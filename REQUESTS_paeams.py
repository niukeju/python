import requests

# 网址：https://www.baidu.com/?wd=python (问号？可有可无)

url = 'https://www.baidu.com/s?'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

p = {'wd':'wd=python'}

response = requests.get(url,headers=headers,params=p)

print(response.content.decode())

# 查看所请求的网站的url -- 需解码（网上使用在线解码工具解码）
 
print(response.request.url)

# 输出：https://www.baidu.com/s?wd=wd%3Dpython

# =================================================================================================

# 使用'{}'.format() 实现带参数请求
import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

url = "https://www.baidu.com/s?wd={}".format("python")

response = requests.get(url,headers=headers)

print(response.request.url)