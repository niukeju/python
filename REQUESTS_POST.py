# 翻译工具

import requests

# 获取百度翻译的网址
url_post = 'https://fanyi.baidu.com/'

# 将百度翻译的头文件赋值给headers
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

# 找到data进行赋值
data = {"from":"en",
        "to":"zh",
        "query":"requests",
        "transtype":"translang",
        "simple_means_flag":"3",
        "sign":"660209.979392",
        "token":"4cd3f77b72dffb14acf0070a94ded9fb",
        "domain":"common"
        }

# 通过post获取信息
response_post = requests.post(url=url_post,data=data,headers=headers)

print(response_post.content.decode())