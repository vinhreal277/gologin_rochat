def profile_identity(profile_name: str, resolution="1920x1080", proxy=None) -> dict:  
    
    return {
        "name": profile_name,
        "notes": "",
        "browserType": "chrome",
        "os": "win",
        "startUrl": "",
        "googleServicesEnabled": False,
        "lockEnabled": False,
        "debugMode": False,
        "navigator": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36",
            "resolution": resolution,
            "language": "en-US,en;q=0.9",
            "platform": "Win32",
            "doNotTrack": False,
            "hardwareConcurrency": 0,
            "deviceMemory": 1,
            "maxTouchPoints": 0
        },
        "geoProxyInfo": {},
        "storage": {
            "local": True,
            "extensions": True,
            "bookmarks": True,
            "history": True,
            "passwords": True,
            "session": True
        },
        "proxyEnabled": True,
        "proxy": {
            "mode": "http",
            "host": "43.159.18.198",
            "port": 22842,
            "username": None,
            "password": None
        },
        "dns": "",
        "plugins": {
            "enableVulnerable": True,
            "enableFlash": True
        },
        "timezone": {
            "enabled": True,
            "fillBasedOnIp": True,
            "timezone": ""
        },
        "audioContext": {
            "mode": "off",
            "noise": 0
        },
        "canvas": {
            "mode": "off",
            "noise": 0
        },
        "fonts": {
            "families": [
                ""
            ],
            "enableMasking": True,
            "enableDomRect": True
        },
        "mediaDevices": {
            "videoInputs": 0,
            "audioInputs": 0,
            "audioOutputs": 0,
            "enableMasking": False
        },
        "webRTC": {
            "mode": "alerted",
            "enabled": True,
            "customize": True,
            "localIpMasking": False,
            "fillBasedOnIp": True,
            "publicIp": "",
            "localIps": [
                ""
            ]
        },
        "webGL": {
            "mode": "noise",
            "getClientRectsNoise": 0,
            "noise": 0
        },
        "clientRects": {
            "mode": "noise",
            "noise": 0
        },
        "webGLMetadata": {
            "mode": "mask",
            "vendor": "",
            "renderer": ""
        },
        "webglParams": [],
        "profile": "",
        "googleClientId": "",
        "updateExtensions": True,
        "chromeExtensions": [
            ""
        ]
    }