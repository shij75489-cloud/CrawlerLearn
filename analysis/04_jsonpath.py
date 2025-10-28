import json

import jsonpath

obj = json.load(open('04_jsonpath.json', 'r', encoding='utf8'))

# 所有书的作者
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)

# 所有作者
author_list = jsonpath.jsonpath(obj, '$..author')
print(author_list)

# store下面所有元素
tag_list = jsonpath.jsonpath(obj, '$.store.*')
print(tag_list)

# store里面所有东西的price
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)

# 第三本书
book = jsonpath.jsonpath(obj, '$..book[2]')
print(book)

# 最后一本书
book = jsonpath.jsonpath(obj, '$..book[(@.length - 1)]')
print(book)

# 前两本书
book_list = jsonpath.jsonpath(obj, '$..book[:2]')
print(book_list)

# 过滤出所有包含isbn的书；条件过滤要加?
book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(book_list)

# 超过10块钱的书
book_list = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(book_list)