from bs4 import BeautifulSoup

# 默认打开文件的编码格式是gbk
soup = BeautifulSoup(open('06_bs4的基本使用.html', encoding='utf-8'), 'lxml')

# 找到的是第一个符合的标签
print(soup.a)
# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数

# find
# 返回第一个a标签
print(soup.find('a'))

print(soup.find('a', title='a2'))
print(soup.find('a', class_='a1'))

print(soup.find_all('a'))

# 返回多个标签，添加列表
print(soup.find_all(['a', 'span']))

print(soup.find_all('li', limit=2))

# select
# 返回多个a
print(soup.select('a'))

# 带class的标签，前面加个点，类选择器
print(soup.select('.a1'))

print(soup.select('#l1'))

# 属性选择器
# li标签中有id属性
print(soup.select('li[id]'))

print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器
print(soup.select('div li')) # 空格代表后代

# 子代选择器
# 某标签的第一子标签
print(soup.select('div > ul > li'))

# 找到a标签和li标签所有的对象
print(soup.select('a,li'))

# 节点信息
obj = soup.select('#d1')[0]
# 标签对象中只有内容，两个都可以用；除了内容还有标签，只能用get_text()
print(obj.get_text())
print(obj.string)

# 节点的属性
obj = soup.select('#p1')[0]
print(obj.name)  # 返回标签名字

obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])











