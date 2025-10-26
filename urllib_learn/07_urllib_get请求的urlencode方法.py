import urllib.parse
import urllib.request

# urlencode应用场景：多个参数的时候

data = {
    'wd' : '周杰伦',
    'sex' : '男',
    'location' : '湖南省'
}

base_url = 'https://www.baidu.com/s?'

new_data = urllib.parse.urlencode(data)

url = base_url + new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #'Accept-Encoding': 'gzip, deflate, br, zstd',  接收的编码格式
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 起决定性作用
    'Cookie': 'BIDUPSID=9ED0AEBE493EDE355700A710E7424659; PSTM=1761374683; BAIDUID=9ED0AEBE493EDE3578AAEF16CE8FA34A:FG=1; BD_UPN=12314753; H_PS_PSSID=64980_65245_65453_65361_65538_65619_65663_65680_65667_65687_65708_65729_65759_65771_65791_65840_65867_65891_65862_65930_65924_65938_65942; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=64980_65245_65453_65361_65538_65619_65663_65680_65667_65687_65708_65729_65759_65771_65791_65840_65867_65891_65862_65930_65924_65938_65942; BAIDUID_BFESS=9ED0AEBE493EDE3578AAEF16CE8FA34A:FG=1; delPer=0; BD_CK_SAM=1; PSINO=6; BA_HECTOR=aha0ah2100al05al2001ah8g0h210m1kfou3324; ZFY=1s3K3IJNyO9VlzvEfSE7oxg9w:Bpq6GYfAbzEOX555hk:C; COOKIE_SESSION=2_0_3_3_0_3_0_0_3_3_0_0_0_0_0_0_0_0_1761376357%7C3%230_0_1761376357%7C1; ab_sr=1.0.1_NTU2ZmE1MjE4NTE2NGZmNzYwMDYzZDQ3MzViNWVhMjRhOTBiYzY2OTcwY2I4NzQwY2VhYmFmZDU2YWNmMmU5MDUyMTc0ZmQ3ZWYyNGZiNjU0ZTdjYTNkM2JjYjM4YzVmNzlmYjFjNDkxNDZiNDI0Y2RjOTZlOGNjYjdhZDY1ODliMzc3NjY0MzQ5MzI2NDdlYzg1NGUwYTdlYWNlYmMwMg==; ppfuid=FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGmVXQmqM6seEAgB/LlOs0+zGEimjy3MrXEpSuItnI4KD7oFvva7GRJFq4qyXFr79ae6x6ODlavYUqwLwpQFMTV+D10st2sQbTMxFLerJlHw3BJsVwXkGdF24AsEQ3K5XBbh9EHAWDOg2T1ejpq0s2eF1B2GaP1HziTgKv97Jkw7/vpaEhZpob9le2b5QIEdiQdtJfhN1eLb/i/C9hcVPjDWFCMUN0p4SXVVUMsKNJv2T2RjO0ZU0bjudHg+LUSELrS4LkPV+7TROLMG0V6r0A++zkWOdjFiy1eD/0R8HcRWYuT+kWCL6ljq7v4YKFUkopCp+HBavJhpxl858h16cMtKQmxzisHOxsE/KMoDNYYE7ucLE22Bi0Ojbor7y6SXfVj7+B4iuZO+f7FUDWABtt/WWQqHKVfXMaw5WUmKnfSR5wwQa+N01amx6X+p+x97kkGmoNOSwxWgGvuezNFuiJQdt51yrWaL9Re9fZveXFsIu/gzGjL50VLcWv2NICayyI8BE9m62pdBPySuv4pVqQ9Sl1uTC//wIcO7QL9nm+0N6JgtCkSAWOZCh7Lr0XP6QztjlyD3bkwYJ4FTiNanaDaDxwHacnQbcy7arAviAQlRhlFBwW2jNiKYvX3gquiRUyhh0GvEV9dnyTGKy8XFjCQiSGk66HDxtjKMU4HPNa0dthF7UsHf7NW9eE+gwuTQSa7GLWfOy9+ap4iFBQsmjpefgOF89jAHLbnVUejtrqqvdVSQ/4gzJOb0DGzeEZ5GeyOKYXqDpIo3DXr5jP0JwWz8rstJ+pP6bN3ZEz8vjHMFncD05kuRm4sFZh/o1XJ6o5ZazU62XvOvycqQeNHJHilKXv+Y0q7CT6wHNqzprY+XMxDln8dKB7nefcEun8dlqoZs4uNOo+pkpyckwWP4VbWloC92vUUtZ2lVqKiGsvJKvLgaUA9sPnxLHpdf4XomqPJzwaYMRRvnyvNvptYm/H9TJ82EtrgcP/nqg17T/hHrOFW2byp/ouxpI4lF8dQtOogBfcrGXrDHbdYEoz55OAGISs/kEn2kikYfHcMOTvlvvnybgKXWVRgHR9zCG7jZoRIJcXe6HpWGsfMtkPHUjgkj; RT="z=1&dm=baidu.com&si=a76ea8ce-9183-4de9-abca-7eb92a68b19c&ss=mh5y07h5&sl=a&tt=97s&bcn=https%3A%2F'
}

request = urllib.request.Request(url=url, headers=headers)  # 关键字传参

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)