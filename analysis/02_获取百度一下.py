import urllib.request

from lxml import etree

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

tree = etree.HTML(content)

# xpath返回值是一个列表
results = tree.xpath("//button[@id='chat-submit-button']/text()")[0]
print(results)