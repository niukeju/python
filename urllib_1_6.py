# 调用urllib.request库
import urllib.request

# 创建变量url，为百度网址
url = 'http://www.baidu.com'

# 创建变量request，模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# 类型：HTTPResponse;方法：read、readline、readlines、getcode、geturl、getheaders.

# 一、类型
# request的类型是HTTPResponse
print(type(response))

# 二、六个方法
# 1、按照一个字节一个字节的去读
content = response.read()

# 只读5个字节
content1 = response.read(5)
print(content1)

# 2、只读一行
content2 = response.readline()
print(content2)

# 3、一行一行去读，直到读完
content3 = response.readlines()
print(content3)

# 4、返回状态码 -- 只有200时证明我们的逻辑没有错
print(response.getcode())

# 5、返回url的地址
print(response.geturl())

# 6、获取一些状态信息
print(response.getheaders())
