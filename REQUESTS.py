import requests
response = requests.get('http://www.baidu.com')

# 查看网址状态
print(response)

# 获取二进制网页数据
print(response.content)

# requests中解决编解码的方法
# 1、使用.decode()方法 -- response.content.decode()
# 修改编码方式：response.content.decode( "utf8”)
print(response.content.decode())

# 2、使用response.text
# 修改编码方式： response.encoding='gbk'
response.encoding = 'utf-8'
print(response.text)