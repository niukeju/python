from base64 import encode
import requests

post_url = 'https://www.huya.com/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

# post_data = {
#     "":""
# }

# 引用requests中的session类，赋值给变量session
session = requests.session()

# 使用session发送post请求，cookies保存其中
session.post(url=post_url,headers=headers)

login_url = 'https://i.huya.com/'

response = session.get(login_url,headers=headers)

# 保存页面
with open('login.html','w',encoding='utf-8') as f:
    f.write(response.content.decode())

