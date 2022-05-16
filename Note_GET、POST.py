# ========================================================================================= #

import requests

#  1、GET请求方式

# url_get赋值为python官网测试网站 -- 格式：‘http://httpbin.org/要测试的请求方式’
url_get = 'http://httpbin.org/get'

# 模拟浏览器请求服务器
response_get = requests.get(url_get)

# 打印返回结果
print(response_get.text)

# ========================================================================================= #

# 2、POST请求

url_post = 'http://httpbin.org/post'
response_post = requests.post(url_post)
print(response_post.text)

# ========================================================================================= #