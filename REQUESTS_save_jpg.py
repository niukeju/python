import requests

# 模拟浏览器向服务器发送请求
response = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')

# 保存
with open('baidu.png','wb') as f:
    f.write(response.content)