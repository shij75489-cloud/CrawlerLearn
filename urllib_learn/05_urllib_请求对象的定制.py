import urllib.request

"""
url的组成
    https://www.baidu.com/s?wd=周杰伦
    http/https      www.baidu.com       80/443      s       wd          #
    协议             主机                 端口号       路径     参数       锚点
"""
url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
}

# 请求对象的定制(解决反派的第一张手段)
request = urllib.request.Request(url=url, headers=headers)  # 关键字传参

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))