import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1761569252678_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'Referer': 'https://dianying.taobao.com/',
    'cookie': 't=c489264b0affbc53dd0158a8cbb42c2f; cookie2=1b6f8b91e676dfd68d06473f70d5e147; v=0; _tb_token_=3be141b1105e6; xlly_s=1; isg=BF9fY3lTS-nUrE_1iE4qi7BW7rPpxLNmIbrEWfGuWo5VgH8C-ZZStpVeQhD-GIve'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8').split('(')[1].split(')')[0]

with open('05_jsonpath解析淘票票.json', 'w', encoding='utf-8') as f:
    f.write(content)

obj = json.loads(open('05_jsonpath解析淘票票.json', 'r', encoding='utf-8').read())
 
city_list = jsonpath.jsonpath(obj, '$..regionName')
print(city_list)