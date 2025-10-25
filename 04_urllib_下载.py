import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'
urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
url_img = '图片地址'
urllib.request.urlretrieve(url_img, '图片.jpg')

# 下载视频
url_video = '视频地址src'
urllib.request.urlretrieve(url_video, '视频.mp4')