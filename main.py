from urllib import request
from lxml import etree
import time
import winsound

pankou1 = set(['平手','平手/半球','半球','半球/一球','一球','一球/球半','球半','球半/两球'])
pankou2 = set(['受平手/半球','受半球','受半球/一球','受一球','受一球/球半','受球半','受球半/两球'])


url="http://live.500.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

def goal_is_who(url):
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read().decode("gbk", 'ignore')
    root = etree.HTML(page_info)
    aa = root.xpath('//table[@class="mtable"]//tr')
    list=[]
    for data in aa:
        if len(data.xpath('./td/img[@src="/images/row/1.gif"]')) != 0:
            list.append(data)
    # for data in list:
    #     if data.xpath('./td/text()')[0] == '\xa0':
    #         print("客队"+data.xpath('./td/text()')[2]+'进球了')
    #     else:
    #         print("主队" + data.xpath('./td/text()')[1] + '进球了')
    if list[0].xpath('./td/text()')[0] == '\xa0':
        #print(list[0].xpath('./td/text()')[2])
        return '客队',list[0].xpath('./td/text()')[2]
    else:
        #print(list[0].xpath('./td/text()')[1])
        return '主队',list[0].xpath('./td/text()')[1]

def readHtml():
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read().decode("gbk", 'ignore')
    # print(page_info)
    root = etree.HTML(page_info)
    aa = root.xpath("//tr[@fid]")
    for data in aa:
        try:
            if data.xpath('./td/div[@class="pk"]/a/text()')[1] in pankou1:
                aaaa, bbbb = goal_is_who(
                    "http://live.500.com/" + data.xpath('./td/div[@class="pk"]/a[@class="fhuise"]/@href')[0])
                if '主队' != aaaa:
                    print('*************重点比赛***************')
                    print(data.xpath('./td/text()')[0])
                    print(data.xpath('./@fid')[0])
                    print(data.xpath('./@gy')[0])
                    # print(data.xpath('./td/div[@class="pk"]/a[@class="fhuise"]/@href')[0])
                    print('主队进球' + data.xpath('./td/div[@class="pk"]/a/text()')[0])
                    print('客队进球' + data.xpath('./td/div[@class="pk"]/a/text()')[2])
                    print('盘口' + data.xpath('./td/div[@class="pk"]/a/text()')[1])
                    print('第一个进球时间' + bbbb)
                    print("==============================================================================")
            if data.xpath('./td/div[@class="pk"]/a/text()')[1] in pankou2:
                aaaa, bbbb = goal_is_who(
                    "http://live.500.com/" + data.xpath('./td/div[@class="pk"]/a[@class="fhuise"]/@href')[0])
                if '客队' != aaaa:
                    print('*************重点比赛***************')
                    print(data.xpath('./td/text()')[0])
                    print(data.xpath('./@fid')[0])
                    print(data.xpath('./@gy')[0])
                    # print(data.xpath('./td/div[@class="pk"]/a[@class="fhuise"]/@href')[0])
                    print('主队进球' + data.xpath('./td/div[@class="pk"]/a/text()')[0])
                    print('客队进球' + data.xpath('./td/div[@class="pk"]/a/text()')[2])
                    print('盘口' + data.xpath('./td/div[@class="pk"]/a/text()')[1])
                    print('第一个进球时间' + bbbb)
                    print("==============================================================================")
            # print(url+data.xpath('./td/div[@class="pk"]/a[@class="fhuise"]/@href')[0])

        except IndexError as e:
            #print("==============================================================================")
            continue

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,60);

while 1==1:
    time.sleep(second);
    readHtml()

















