# natas8

import requests
from pwn import log
from base64 import b64decode
from binascii import unhexlify
import re

url = 'http://natas8.natas.labs.overthewire.org'
username = "natas8"
password = "xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q"
auth = (username, password)
enc_secret = "3d3d516343746d4d6d6c315669563362"

def decode_secret(secret):
    res = b64decode(unhexlify(secret)[::-1])
    return res

def exploit():
    secret = decode_secret(enc_secret)
    log.info('Secret : %s', secret.decode())

    data = {
        'secret': {secret.decode()},
        'submit': 'Submit'
    }

    res = requests.post(url, data=data, auth=auth)
    flag = re.findall('.*natas9.*', res.text)
    log.info(flag)


if __name__ == '__main__':
    exploit()

# natas9:ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t