import urllib.request

"""
个人页面信息是utf-8，但还是报编码错误，因为没有进入到个人信息页面，而是跳转到了登录页面
登录页面不是utf-8，所以报错
"""

url = 'https://weibo.cn/6473405331/info'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'cookie' : '_T_WM=427daa9abd368b9d6014ca690a19347a; SCF=AuBfdarijzC5_63zElR13HGeLBKkHTbHo_tasYuRxZrxazLKrbJ_6wEAImqjocHUzQhUhabTNXQjvrRU-tORiFc.; SUB=_2A25F-bABDeRhGeBK7FEV8CvPyD2IHXVnd03JrDV6PUJbktAbLXPbkW1NR4VuD1xD_jvghdwIb6fvAPE8ApdlRYto; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW6hGlkP-EPqpzkMqB8LjlQ5NHD95QcShM0Sh5fe0epWs4Dqcjgi--ciKn4i-zci--fi-zpi-zpPcLr95tt; SSOLoginState=1761460305; ALF=1764052305'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

with open('weibo.html','w',encoding='utf-8') as f:
    f.write(content)