import requests

url = 'https://www.sina.com.cn/'

response = requests.get(url)

print(response.text)

print(response.content.decode())
