import urllib.request
import urllib.parse


# https://www.baidu.com/s?wd=周杰伦 获取该网页的源码

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
}

# 将周杰伦三个字变为unicode编码
name = urllib.parse.quote('周杰伦')
url += name

# 请求对象的定制
#被反爬了
request = urllib.request.Request(url=url, headers=headers)  # 关键字传参

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)