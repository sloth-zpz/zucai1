from urllib import request
from lxml import etree
import time
import itchat

pankou1 = set(['平手','平手/半球','半球','半球/一球','一球','一球/球半','球半','球半/两球'])
pankou2 = set(['受平手/半球','受半球','受半球/一球','受一球','受一球/球半','受球半','受球半/两球'])


url="http://live.500.com/2h1.php"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

itchat.auto_login(hotReload=True)

user = itchat.search_friends(name=u'自然醒')[0]

def goal_is_who(url):
    page = request.Request(url)
    page_info = request.urlopen(page).read().decode("gbk", 'ignore')
    root = etree.HTML(page_info)
    aa = root.xpath('//table[@class="mtable"]//tr')
    list=[]
    for data in aa:
        if len(data.xpath('./td/img[@src="/images/row/1.gif"]'))+len(data.xpath('./td/img[@src="/images/row/2.gif"]'))+len(data.xpath('./td/img[@src="/images/row/3.gif"]')) != 0:
            list.append(data)
    # for data in list:
    #     if data.xpath('./td/text()')[0] == '\xa0':
    #         print("客队"+data.xpath('./td/text()')[2]+'进球了')
    #     else:
    #         print("主队" + data.xpath('./td/text()')[1] + '进球了')
    if list[0].xpath('./td/text()')[0] == '\xa0':
        return '客队',list[0].xpath('./td/text()')[2][:-1]
    else:
        return '主队',list[0].xpath('./td/text()')[1][:-1]

def readHtml():
    page = request.Request(url)
    page_info = request.urlopen(page).read().decode("gbk", 'ignore')
    root = etree.HTML(page_info)
    aa = root.xpath("//tr[@yy]")
    for data in aa:
        try:
            ############################完场统计###################################
            #if data.xpath('./td/span[@class="red"]/text()')[0] == '完':
            ############################正在进行的比赛#############################
            if len(data.xpath('./td/span[@class="red"]/text()')) == 0:
                jicaiID = data.xpath('./td/text()')[0]
                num = data.xpath('./@id')[0][1:]
                duiwu = data.xpath('./@gy')[0]
                num_zhu = data.xpath('./td/div[@class="pk"]/a/text()')[0]
                num_ke = data.xpath('./td/div[@class="pk"]/a/text()')[2]
                pankou = data.xpath('./td/div[@class="pk"]/a/text()')[1]
                if data.xpath('./td/div[@class="pk"]/a/text()')[1] in pankou1:
                    aaaa, bbbb = goal_is_who(
                        "http://live.500.com/detail.php?fid="+num+"&r=1")
                    if '主队' != aaaa:
                        if int(bbbb) <= 45:
                            print('*************重点比赛***************')
                            print(jicaiID)
                            print(num)
                            print(duiwu)
                            print('主队进球' + num_zhu)
                            print('客队进球' + num_ke)
                            print('盘口' + pankou)
                            print('第一个进球时间' + bbbb)

                            itchat.send_msg("**********" + jicaiID + "**********"+"\n"
                                            +duiwu+"\n"
                                            +"盘口:" + pankou+"\n"+
                                            "比分:" + num_zhu + "-" + num_ke+"\n"
                                            +'第一个进球时间' + bbbb+"(客队)", "filehelper")

                            user.send("**********" + jicaiID + "**********" + "\n"
                                            + duiwu + "\n"
                                            + "盘口:" + pankou + "\n" +
                                            "比分:" + num_zhu + "-" + num_ke + "\n"
                                            + '第一个进球时间' + bbbb + "(客队)")
                            print("==============================================================================")
                if data.xpath('./td/div[@class="pk"]/a/text()')[1] in pankou2:
                    aaaa, bbbb = goal_is_who(
                        "http://live.500.com/detail.php?fid="+data.xpath('./@fid')[0]+"&r=1")
                    if int(bbbb) <= 45:
                        if '客队' != aaaa:
                            print('*************重点比赛***************')
                            print(jicaiID)
                            print(num)
                            print(duiwu)
                            print('主队进球' + num_zhu)
                            print('客队进球' + num_ke)
                            print('盘口' + pankou)
                            print('第一个进球时间' + bbbb)

                            itchat.send_msg("**********" + jicaiID + "**********" + "\n"
                                            + duiwu + "\n"
                                            + "盘口:" + pankou + "\n" +
                                            "比分:" + num_zhu + "-" + num_ke + "\n"
                                            + '第一个进球时间' + bbbb + "(主队)", "filehelper")

                            user.send("**********" + jicaiID + "**********" + "\n"
                                            + duiwu + "\n"
                                            + "盘口:" + pankou + "\n" +
                                            "比分:" + num_zhu + "-" + num_ke + "\n"
                                            + '第一个进球时间' + bbbb + "(客队)")
                            print("==============================================================================")

        except IndexError as e:
            #print("==============================================================================")
            continue

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,60);

readHtml()
while 1==1:
    time.sleep(second);
    readHtml()
    itchat.send_msg("============================", "filehelper")
    user.send("============================")
