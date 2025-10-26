import urllib.request
from lxml import etree


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'cookie' : 'cz_statistics_visitor=9d71e868-9d7f-02d8-1bdf-7409b792d1e2; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1761485604; HMACCOUNT=B12790C64C7EEDBA; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1761486082'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(content):
    tree = etree.HTML(content)
    # //div[@class="container"]//div[@class="item masonry-brick"]/img/@src
    name_list = tree.xpath('//div[@class="container"][2]//div[@class="item masonry-brick"]/img/@src')

    # 一般设计图片的网站都会进行懒加载
    # 使用懒加载之前的xpath路径
    src_list = tree.xpath('//div[@class="container"][2]//div[@class="item masonry-brick"]/img/@src2')

    for i in range(len(name_list)):
        url = 'https:' + src_list[i]

        urllib.request.urlretrieve(url=url, filename=name_list[i] + '.png')


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(content)