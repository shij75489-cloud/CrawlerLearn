import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'http': 'http://127.0.0.1:1080',
}

handler = urllib.request.ProxyHandler(proxies={})

opener = urllib.request.build_opener(handler)

response = opener.open(request)

print(response.read().decode('utf-8'))