import urllib.request

# 获取百度首页的源码
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 获取响应中页面的源码
# read方法返回的是字节形式的二进制数据
# 二进制->字符串 decode解码
content = response.read().decode('utf-8')

# 打印数据
print(content)