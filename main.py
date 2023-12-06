from playwright.sync_api import sync_playwright
import requests
import json
from profile_identity import profile_identity
from concurrent.futures import ThreadPoolExecutor
from get_code_fastmail import get_code


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTAyMGFkMDEwNThjM2NiZjY5MGQ3ZjIiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTAzY2UzMDQ2ZDJmMTQ4ZDY4NzFmZTgifQ.Rr71NMR007oBZwrG-6Q75AMquMdhX3sSZP9AQQC-VeY"


def create_profile(profile_name: str):
    """ Create a new profile in GoLogin and return the profile ID """
    
    url = "https://api.gologin.com/browser"
    headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    
    data = profile_identity(profile_name, resolution="920x1080")
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        id = response.json()["id"]
        return id

    except Exception as e:
        print(e)


def run_profile(profile_id: str):
    """ Run a profile in GoLogin """
        
    url = "http://localhost:36912/browser/start-profile"
    headers = {
        "Content-Type": "application/json"
        }
    body = {
        "profileId": profile_id,
        "sync": True,
        }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(body))
        wsUrl = response.json()["wsUrl"]
        return wsUrl
    except Exception as e:
        print(e)


def control_browser(wsUrl: str, email: str):  
    try:
        with sync_playwright() as playwright:
            
            browser = playwright.chromium.connect_over_cdp(wsUrl)
            context = browser.contexts[0]
            page = context.pages[0]
            page.goto("https://rochat.ai/inviteTo?code=296YFX")
            page.click("text=Login and redeem")
            page.click("text=Continue with Email")
            page.locator('(//input[@placeholder="Email address"])[1]').fill(email)
            page.wait_for_selector("text=Send code").click()
            page.wait_for_timeout(10000)
            verification_code = get_code(email)
            print(verification_code)
            page.wait_for_timeout(2000)
            
            if not verification_code or verification_code == "None":
                print("Verification code not found")
                browser.close()
                return
            
            page.wait_for_selector("//input[@placeholder='Enter the Verification Code']").type(verification_code, delay=100)
            page.click("text=Continue")
            page.wait_for_selector("text=Redeem").click()
            page.wait_for_selector("text=Confirm").click()
            page.wait_for_timeout(3000)
            browser.close()
            
    except (TimeoutError, Exception) as e:
        print(e)
        browser.close()
            

def stop_profile(profile_id: str):
    url = "http://localhost:36912/browser/stop-profile"
    headers = {
        "Content-Type": "application/json"
        }
    body = {
        "profileId": profile_id,
        }
    requests.post(url, headers=headers, data=json.dumps(body))


def delete_profile(profile_id):
    url = f'https://api.gologin.com/browser/{profile_id}'
    headers = {
            "Authorization": f"Bearer {TOKEN}",
        }
    try:
        requests.delete(url, headers=headers)
    except Exception as e:
        print(e)

def get_email():
    with open ("emails.txt", "r") as f:
        emails = f.readlines()
        return [email.strip() for email in emails]

def main(email):
    profile_id = create_profile(email)
    wsUrl = run_profile(profile_id)
    control_browser(wsUrl, email)
    stop_profile(profile_id)
    delete_profile(profile_id)
    

if __name__ == "__main__":
    emails = get_email()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for email in emails:
            executor.submit(main, email)
    
            
