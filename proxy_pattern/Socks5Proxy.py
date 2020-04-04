# pip install PySocks

import requests

url = 'https://www.google.com'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
proxies = {'http':'socks5://localhost:1080','https':'socks5://localhost:1080'}
response = requests.get(url,proxies=proxies, headers=headers,verify=True)
print(response.text)
