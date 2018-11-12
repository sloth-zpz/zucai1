from urllib import request
from lxml import etree
#import itchat
import pymysql
import time
import io
import gzip
import datetime

import tongji

pankou1 = set(['平手','平手/半球','半球','半球/一球','一球','一球/球半','球半','球半/两球'])
pankou2 = set(['受平手/半球','受半球','受半球/一球','受一球','受一球/球半','受球半','受球半/两球'])


#url="http://live.500.com/?e=2018-06-03"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

#itchat.auto_login(hotReload=True)

#user = itchat.search_friends(name=u'自然醒')[0]
#user1 = itchat.search_friends(name=u'薛昊')[0]

def getBetweenDay(begin_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d',time.localtime(time.time())), "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


def goal_is_who(url):
    page = request.Request(url)
    data = request.urlopen(page)
    encoding = data.getheader('Content-Encoding')
    content = data.read()
    if encoding == 'gzip':
        buf = io.BytesIO(content)
        gf = gzip.GzipFile(fileobj=buf)
        content = gf.read()
    page_info = content.decode("gb2312", 'ignore')
    root = etree.HTML(page_info)
    aa = root.xpath('//table[@class="mtable"]//tr')
    list=[]
    for data in aa:
        if len(data.xpath('./td/img[@src="/images/row/1.gif"]'))+len(data.xpath('./td/img[@src="/images/row/2.gif"]'))+len(data.xpath('./td/img[@src="/images/row/3.gif"]')) != 0:
            list.append(data)
    num_zhu = 0
    num_ke = 0
    str_goal = ""
    first_goal_time = 0
    for data in list:
        if data.xpath('./td/text()')[0] == '\xa0':
            num_ke += 1
            str_goal = str_goal + str(data.xpath('./td/text()')[2][:-1]) + "分 " + str(num_zhu) + "-" + str(num_ke) + ','
        else:
            if len(list[0].xpath('./td/text()')) == 3:
                num_zhu += 1
                str_goal = str_goal + str(data.xpath('./td/text()')[0][:-1]) + "分 " + str(num_zhu) + "-" + str(num_ke) + ','
            else:
                num_zhu += 1
                str_goal = str_goal + str(data.xpath('./td/text()')[1][:-1]) + "分 " + str(num_zhu) + "-" + str(num_ke) + ','
    if list[0].xpath('./td/text()')[0] == '\xa0':
        return '客队',list[0].xpath('./td/text()')[2][:-1],str_goal
    else:
        if len(list[0].xpath('./td/text()')) == 3:
            return '主队',list[0].xpath('./td/text()')[0][:-1],str_goal
        else:
            return '主队',list[0].xpath('./td/text()')[1][:-1],str_goal

def readHtml(url_home,date):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "gunxifacai",charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    page = request.Request(url_home)

    data = request.urlopen(page)
    encoding = data.getheader('Content-Encoding')
    content = data.read()
    if encoding == 'gzip':
        buf = io.BytesIO(content)
        gf = gzip.GzipFile(fileobj=buf)
        content = gf.read()
    page_info = content.decode("gb2312", 'ignore')
    root = etree.HTML(page_info)
    aa = root.xpath("//tr[@yy]")
    for data in aa:
        try:
            ############################完场统计###################################
            if data.xpath('./td/span[@class="red"]/text()')[0] == '完':
            ############################正在进行的比赛#############################
            #if len(data.xpath('./td/span[@class="red"]/text()')) == 0:
                jicaiID = data.xpath('./td/text()')[0]
                num = data.xpath('./@id')[0][1:]
                duiwu = data.xpath('./@gy')[0]
                game = str(duiwu).split(',')
                game_name = game[0]
                zhu_name = game[1]
                ke_name = game[2]
                num_zhu = data.xpath('./td/div[@class="pk"]/a/text()')[0]
                num_ke = data.xpath('./td/div[@class="pk"]/a/text()')[2]
                pankou = data.xpath('./td/div[@class="pk"]/a/text()')[1]
                if data.xpath('./td/div[@class="pk"]/a/text()')[1] in pankou1:
                    aaaa, bbbb,str_goal = goal_is_who(
                        "http://live.500.com/detail.php?fid="+num+"&r=1")
                    if '主队' != aaaa:
                        if int(bbbb) <= 100:
                            if insert_recode(cursor,num, jicaiID, game_name,zhu_name,ke_name,bbbb, num_zhu, num_ke, pankou,str_goal,str(tongji.tongji(int(num_zhu), int(num_ke), pankou)),date):
                                message = "**********" + jicaiID + "**********" + "\n"+duiwu + "\n"+\
                                          "盘口:" + pankou + "\n" +"(客队先进球)" + "\n" +str_goal + "\n"+\
                                          "目前" + str(tongji.tongji(int(num_zhu), int(num_ke), pankou)) + "手"
                                #itchat.send_msg(message,"filehelper")
                                print('*************重点比赛***************')
                                print(message)
                            print("==============================================================================")
                if data.xpath('./td/div[@class="pk"]/a/text()')[1] in pankou2:
                    aaaa, bbbb,str_goal = goal_is_who(
                        "http://live.500.com/detail.php?fid="+data.xpath('./@fid')[0]+"&r=1")
                    if int(bbbb) <= 100:
                        if '客队' != aaaa:
                            if insert_recode(cursor,num, jicaiID, game_name,zhu_name,ke_name,bbbb, num_zhu, num_ke, pankou,str_goal,str(tongji.tongji(int(num_zhu), int(num_ke), pankou)),date):
                                message = "**********" + jicaiID + "**********" + "\n" + duiwu + "\n" + \
                                          "盘口:" + pankou + "\n" + "(主队先进球)" + "\n" + str_goal + "\n" + \
                                          "目前" + str(tongji.tongji(int(num_zhu), int(num_ke), pankou)) + "手"
                                #itchat.send_msg(message, "filehelper")
                                print('*************重点比赛***************')
                                print(message)
                            print("==============================================================================")

        except IndexError as e:
            #print("==============================================================================")
            continue
    db.commit()
    db.close()
def insert_recode(cursor,num,jicaiID,game_name,zhu_name,ke_name,first_goal_time,num_zhu,num_ke,pankou,str_goal,win,date):
    num_zhu = int(num_zhu)
    num_ke = int(num_ke)
    first_goal_time=int(first_goal_time)
    sql = "SELECT * FROM gunqiu where id='%s'"%(num)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        #print(results)
        if len(results) == 0:
            sql = "INSERT INTO gunqiu(id, \
                jingcai_id, game_name,zhu_name,ke_name,first_goal_time, goal_z, goal_k,pankou,goal_detail,win,date) \
                VALUES ('%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d','%s','%s','%s', '%d' )" % \
                (num,jicaiID,game_name,zhu_name,ke_name,first_goal_time,num_zhu,num_ke,pankou,str_goal,win,date)
            # print(sql)
            cursor.execute(sql)
            return True
        else:
            zhu = results[0][3]
            ke =results[0][4]
            if (zhu !=num_zhu) | (ke != num_ke):
                sql = "UPDATE gunqiu SET goal_z = '%d',goal_k = '%d',goal_detail='%s',first_goal_time='%d',win='%s' WHERE id = '%s'" % (num_zhu,num_ke,str_goal,first_goal_time,win,num)
                cursor.execute(sql)
                return True
            return False

    except Exception as e:
        print(e)

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,60);

# print("1、阿根廷的联赛不买")
# print("2、小孩的比赛少买")
# print("3、澳洲的比赛不买让球盘，只买大小球")
# print("4、买前看五分钟比赛数据")
# readHtml()

for date in getBetweenDay('2018-11-01'):
    url = "http://live.500.com/?e="+date
    mysql_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    date_int = int(mysql_date.strftime("%Y%m%d"))
    print(url)
    readHtml(url,date_int)

# while 1==1:
#     time.sleep(second);
#     readHtml()
    #itchat.send_msg("============================", "filehelper")
    #user.send("============================")
