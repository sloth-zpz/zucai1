from new import http_to_char
from lxml import etree

__all__ = [
    'get_ouzhi',
    'get_yazhi'
]

def get_ouzhi(url):
    content = http_to_char.get_content_by_url(url)
    root = etree.HTML(content)

    ouzhi_str = ""
    ouzhi = []
    born_3 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr[1]/td[1]/text()')[0]
    born_1 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr[1]/td[2]/text()')[0]
    born_0 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr[1]/td[3]/text()')[0]
    ouzhi.append([born_3,born_1,born_0])

    dead_3 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr[2]/td[1]/text()')[0]
    dead_1 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr[2]/td[2]/text()')[0]
    dead_0 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr[2]/td[3]/text()')[0]
    ouzhi.append([dead_3, dead_1, dead_0])

    ceri_born_3 = root.xpath('//*[@id="3"]/td[6]/table/tbody/tr[1]/td[1]/text()')[0]
    ceri_born_1 = root.xpath('//*[@id="3"]/td[6]/table/tbody/tr[1]/td[2]/text()')[0]
    ceri_born_0 = root.xpath('//*[@id="3"]/td[6]/table/tbody/tr[1]/td[3]/text()')[0]
    ouzhi.append([ceri_born_3, ceri_born_1, ceri_born_0])

    ceri_dead_3 = root.xpath('//*[@id="3"]/td[6]/table/tbody/tr[2]/td[1]/text()')[0]
    ceri_dead_1 = root.xpath('//*[@id="3"]/td[6]/table/tbody/tr[2]/td[2]/text()')[0]
    ceri_dead_0 = root.xpath('//*[@id="3"]/td[6]/table/tbody/tr[2]/td[3]/text()')[0]
    ouzhi.append([ceri_dead_3, ceri_dead_1, ceri_dead_0])

    # for data in ouzhi:
    #     ouzhi_str += data[0]+","+data[1]+","+data[2]+"|"
    #
    # return ouzhi_str
    return ouzhi

def get_yazhi(url):
    content = http_to_char.get_content_by_url(url)
    root = etree.HTML(content)

    yazhi = []
    yazhi_str = ""
    born_3 = root.xpath('//*[@id="3"]/td[5]/table/tbody/tr/td[1]/text()')[0]
    born_1 = root.xpath('//*[@id="3"]/td[5]/table/tbody/tr/td[2]/text()')[0]
    born_0 = root.xpath('//*[@id="3"]/td[5]/table/tbody/tr/td[3]/text()')[0]
    yazhi.append([born_3, born_1, born_0])

    dead_3 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr/td[1]/text()')[0]
    dead_1 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr/td[2]/text()')[0]
    dead_0 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr/td[3]/text()')[0]
    yazhi.append([dead_3, dead_1, dead_0])

    # for data in yazhi:
    #     yazhi_str += data[0]+","+data[1]+","+data[2]+"|"
    # return yazhi_str
    return yazhi

def get_daxiao(url):
    content = http_to_char.get_content_by_url(url)
    root = etree.HTML(content)

    daxiao = []
    daxiao_str = ""
    born_3 = root.xpath('//*[@id="3"]/td[5]/table/tbody/tr/td[1]/text()')[0]
    born_1 = root.xpath('//*[@id="3"]/td[5]/table/tbody/tr/td[2]/text()')[0]
    born_0 = root.xpath('//*[@id="3"]/td[5]/table/tbody/tr/td[3]/text()')[0]
    daxiao.append([born_3, born_1, born_0])

    dead_3 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr/td[1]/text()')[0]
    dead_1 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr/td[2]/text()')[0]
    dead_0 = root.xpath('//*[@id="3"]/td[3]/table/tbody/tr/td[3]/text()')[0]
    daxiao.append([dead_3, dead_1, dead_0])

    # for data in daxiao:
    #     daxiao_str += data[0]+","+data[1]+","+data[2]+"|"
    # return daxiao_str

    return daxiao



