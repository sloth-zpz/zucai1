from oupei import http_to_char
from lxml import etree

list = ["竞彩官方","威廉希尔","澳门","立博","Bet365","Interwetten","SNAI","皇冠","易胜博","伟德",
        "Bwin","Gamebookers","Pinnacle平博","10BET","Coral","利记","Unibet (优胜客)","SportingBet (博天堂)",
        "IBCBET (沙巴)","Mansion88 (明升)"]
def get_oupei(game_id):
    url = 'http://odds.500.com/fenxi/ouzhi-' + game_id + '.shtml'
    content = http_to_char.get_content_by_url(url)
    root = etree.HTML(content)
    result_list = []
    for bet_company in list:
        one = root.xpath('//*[@title="'+ bet_company + '"]/..')
        if len(one) == 0:
            get_data_simple(result_list)
        else:
            get_data(one[0],result_list)
    return result_list

def get_data(one,result_list):
    l1 = float(one.xpath('./td[3]/table/tbody/tr[1]/td[1]/text()')[0])/3
    l2 = float(one.xpath('./td[3]/table/tbody/tr[1]/td[2]/text()')[0])/3
    l3 = float(one.xpath('./td[3]/table/tbody/tr[1]/td[3]/text()')[0])/3

    m1 = float(one.xpath('./td[3]/table/tbody/tr[2]/td[1]/text()')[0])/3
    m2 = float(one.xpath('./td[3]/table/tbody/tr[2]/td[2]/text()')[0])/3
    m3 = float(one.xpath('./td[3]/table/tbody/tr[2]/td[3]/text()')[0])/3

    k1 = float(one.xpath('./td[6]/table/tbody/tr[1]/td[1]/text()')[0]) / 3
    k2 = float(one.xpath('./td[6]/table/tbody/tr[1]/td[2]/text()')[0]) / 3
    k3 = float(one.xpath('./td[6]/table/tbody/tr[1]/td[3]/text()')[0]) / 3

    n1 = float(one.xpath('./td[6]/table/tbody/tr[2]/td[1]/text()')[0]) / 3
    n2 = float(one.xpath('./td[6]/table/tbody/tr[2]/td[2]/text()')[0]) / 3
    n3 = float(one.xpath('./td[6]/table/tbody/tr[2]/td[3]/text()')[0]) / 3

    for i in [l1,l2,l3,m1,m2,m3,k1,k2,k3,n1,n2,n3]:
        result_list.append(i)

def get_data_simple(result_list):
    l1 = 1.0/3.0
    l2 = 1.0/3.0
    l3 = 1.0/3.0

    m1 = 1.0/3.0
    m2 = 1.0/3.0
    m3 = 1.0/3.0

    k1 = 0.92
    k2 = 0.92
    k3 = 0.92

    n1 = 0.92
    n2 = 0.92
    n3 = 0.92

    for i in [l1,l2,l3,m1,m2,m3,k1,k2,k3,n1,n2,n3]:
        result_list.append(i)

