import requests

url = ''

response = requests.get(url)

with open('第一集.MP4','wb') as f:
    f.write(response.content)