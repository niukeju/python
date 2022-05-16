# 下载图片实例操作
'''
    下载图片操作步骤：
        1、引入requests库 -- import
        2、变量赋值 要下载图片的网址 -- url = '网址'
        3、设置文件的headers -- headers = { "User-Agent":"UserActivation 'F12 Consels'" }
        4、使用get()模仿浏览器向服务器发送请求 -- response = requests.get(url,headers)
        5、赋值变量 将网址切割 -- url.split('/')[-1]
        6、使用with……as输出图片 -- with open(文件名,'写入格式') as f:
                                        f.write(response.content)
                                        print('写入成功')
'''

# 引用requests库
import requests

# 输入要下载图片的网址
url = 'https://wx4.sinaimg.cn/mw690/006HJgYYgy1h12v5hnlh6g30dl0dlqv5.gif'

# 设置文件的头文件
headers = {
    "User-Agent":"UserActivation {hasBeenActive: true, isActive: true}"
}

# 模仿浏览器请求服务器
response = requests.get(url=url,headers=headers)

# 将网址切割（这里需要的是url的最后一段“006HJgYYgy1h12v56g30dl05.gif”）
file_name = url.split('/')[-1]

# open() -- 括号内参数：
# 文件名，写入格式(wb为二进制写入)，
with open(file_name,'wb',) as f:
    f.write(response.content)
    print('写入成功')
