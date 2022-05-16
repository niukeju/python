import requests
import json

url_post = 'https://fanyi.baidu.com/'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

data = {
    "from": "zh",
    "to": "en",
    "query": "我爱李雅",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "86749.373228",
    "token": "4cd3f77b72dffb14acf0070a94ded9fb",
    "domain": "common"
}

response = requests.post(url=url_post,headers=headers,data=data)

print(response.content.decode())
