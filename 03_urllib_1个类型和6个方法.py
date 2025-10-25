import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 返回多少个字节
response.read(5)

# 读取一行
response.readline()

# 返回状态码
response.getcode()

# 返回url
response.geturl()

# 获取一个状态信息
response.getheaders()