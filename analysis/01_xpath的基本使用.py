from lxml import etree

"""
xoath解析
    1、本地文件  etree.parse
    2、服务器响应的数据  etree.HTML
    
    //：查找所有子孙节点
    //：直接找子节点
    
    
"""

# 解析本地文件
tree = etree.parse('01_xpath的基本使用.html')

# 查找ul下面的li
li_list = tree.xpath('//body/ul/li')
for li in li_list:
    print(li.text)

# 查找所有有id属性的li标签
li_list = tree.xpath('//ul/li[@id]/text()')
print(li_list)

li_list = tree.xpath('//ul/li[@id="id1"]/text()')
print(li_list)

# 查找到id为id1的li标签的class属性值
li = tree.xpath('//ul/li[@id="id1"]/@class')
print(li)

# 查找id包含id的li标签
li_list = tree.xpath('//ul/li[contains(@id,"id")]/text()')
print(li_list)

li_list = tree.xpath('//ul/li[starts-with(@id,"i")]/text()')
print(li_list)

# 逻辑运算
li_list = tree.xpath('//ul/li[@id="id1" and @class="c1"]/text()')
print(li_list)

li_list = tree.xpath('//ul/li[@id="id1"]/text() | //ul/li[@id="id2"]/text()')
print(li_list)