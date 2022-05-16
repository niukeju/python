# 引用requests库
import requests

# 赋值给url百度的网址
url = 'http://www.baidu.com'

# 设置头文件
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

# 设置代理IP
proxies = {
    "https":"https:46.35.249.189:41419"
}

# 模拟浏览器向服务器发送请求，请求返回给response
response = requests.get(url=url,headers=headers,proxies=proxies)

# 打印response状态（200为正常）
print(response)

# 打印返回结果
print(response.content.decode())

