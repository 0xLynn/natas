# natas11

import requests
from pwn import log
import re
import base64
import json

url = 'http://natas11.natas.labs.overthewire.org'
username = "natas11"
password = "UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk"
auth = (username, password)
data = '{ "showpassword":"no","bgcolor":"#ffffff"}'

def xor(text, key):
        return ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))
def exploit():
    json_str = json.dumps(data)
    enc_json = base64.b64encode(json_str.encode()).decode()
    log.info("plain cookie : %s", enc_json)

    session = requests.Session()
    session = session.get(url, auth=auth)
    cookies = session.cookies.get('data')
    log.info('Encoded Cookie : %s', cookies)

    cookies = cookies.replace('%3D', '=')
    cipher = base64.b64decode(cookies)
    log.info(cipher)
    key = xor()
    # log.info('Key : %s', key)

    enc_data = xor(data, key)
    cookies = base64.b64encode(enc_data.encode()).decode()
    log.info('New cookie = %s', cookies)

    cookies = {
        'data': cookies
    }

    res = requests.get(url, auth=auth, cookies=cookies)
    # log.info(res.text)

if __name__ == '__main__':
    exploit()
    
# 