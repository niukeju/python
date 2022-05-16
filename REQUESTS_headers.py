import requests

url = 'http://www.baidu.com'

# 设置请求头文件 -- 作用：模仿浏览器
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

response = requests.get(url,headers = headers)

# print(response.request.headers)

print(response.content.decode())