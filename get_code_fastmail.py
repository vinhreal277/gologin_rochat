import requests
import json
import re


TOKEN = 'fmu1-07f94065-ce40458079e5e01adc9c12d532ab8d0e-0-0515aac4ebf9ca6afc97cb4d2f108183'
ACCOUNT_ID = 'u07f94065'


def get_info():
    url = 'https://api.fastmail.com/jmap/session'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {TOKEN}'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Print the formatted response content
        print(json.dumps(response.json(), indent=4))
        

def get_message_data(quantity=5):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f"Bearer {TOKEN}"
    }
    
    payload = {
        'using': ["urn:ietf:params:jmap:core", "urn:ietf:params:jmap:mail"],
        'methodCalls': [
            ['Email/query',
             {
                 'accountId': ACCOUNT_ID,
                 # 'filter': {'inMailbox': inbox_id},
                 'sort': [{'property': "receivedAt", 'isAscending': False}],
                 'limit': quantity
             },
             'a'
             ],
            
            ['Email/get',
             {
                 'accountId': ACCOUNT_ID,
                 'properties': ['subject', 'receivedAt', 'from', 'to', 'preview'],
                 '#ids': {
                     'resultOf': 'a',
                     'name': 'Email/query',
                     'path': '/ids/*'
                 }
             },
             'b'
             ]
        ]
    }
    
    response = requests.post('https://api.fastmail.com/jmap/api/', headers=headers, json=payload)
    data = response.json()    
    return data
    
def extract_data(data, email):
    list_message = data['methodResponses'][1][1]['list']
    for message in list_message:
        sender = message['from'][0]['email']
        sender_name = message['from'][0]['name']
        receiver = message['to'][0]['email']
        time_received = message['receivedAt']
        subject = message['subject']
        # preview = message['preview']
        
        if 'rochat' in sender and email in receiver:
            preview = message['preview']
            pattern = r"\d{4}"
            matches = re.findall(pattern, preview)
            return matches[0]
        else:
            continue

def get_email():
    with open ("emails.txt", "r") as f:
        emails = f.readlines()
        return emails

    
def get_code(email):
    data = get_message_data(quantity=20)
    code = extract_data(data, email)
    print(code)
    return str(code).strip()



    




        

