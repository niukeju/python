print('-'*70)
# ================================================== #

import requests
url_post = 'http://httpbin.org/post'
response_post = requests.post(url_post)

# Requests参数

# 1、显示二进制内容 -- content
con = response_post.content
print(con)
print(type(con))

# ================================================== #
print('-'*70)
# ================================================== #

# 2、对二进制内容进行解码 -- decode
d = response_post.content.decode()
print(d)
print(type(d))

# ================================================== #
print('-'*70)
# ================================================== #

# 3、将读取到的内容转换为字典格式 -- json
j = response_post.json()
print(j)
print(type(j))

# ================================================== #
print('-'*70)
# ================================================== #

# 4、返回状态 -- status_code
s = response_post.status_code
print(s)
print(type(s))

# ================================================== #
print('-'*70)
# ================================================== #

# 5、服务器返回的headers -- headers
h = response_post.headers
print(h)
print(type(h))

# ================================================== #
print('-'*70)
# ================================================== #

# 6、获取网址 -- url
u = response_post.url
print(u)
print(type(u))

# ================================================== #
print('-'*70)
# ================================================== #

# 7、验证请求前的信息 -- request
r1 = response_post.request.url
r2 = response_post.request.headers
print(r1)
print(r2)

# ================================================== #
print('-'*70)
# ================================================== #

print(response_post.text)
print(type(response_post.text))

# ================================================== #
print('-'*70)
# ================================================== #