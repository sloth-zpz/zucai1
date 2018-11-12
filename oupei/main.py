from oupei import game_list
import pymysql
import pickle
import datetime
import time

# # 打开数据库连接
# db = pymysql.connect("localhost","root","123456","gunxifacai",charset="utf8")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()

def getBetweenDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

def get_url_list():
    list_urls = []
    list = getBetweenDay('2018-10-21','2018-10-21')
    for date in list:
        list_urls.append('http://live.500.com/?e='+date)
    return list_urls

# def insert(result):
#     for item in result:
#         if item[7] != 0:
#             sql = "insert into shijiebei(id,game,changci,name_zhu,name_ke,whole,half," \
#                   "first_goal_team,first_goal_time,goal_decs)" \
#                   "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',%d,'%s')" % \
#                   (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[8],int(item[9]),item[10])
#             print(sql)
#             cursor.execute(sql)
#         else:
#             sql = "insert into shijiebei(id,game,changci,name_zhu,name_ke,half,whole)" \
#                   "VALUES ('%s','%s','%s','%s','%s','%s','%s')" % \
#                   (item[0], item[1], item[2], item[3], item[4], item[5], item[6])
#             cursor.execute(sql)
#     db.commit()
#
# def update(num,ouzhi,yazhi,daxiao):
#     sql = "update shijiebei t set ouzhi='%s',yazhi='%s',daxiao='%s'" \
#           " where t.id='%s'" % (ouzhi,yazhi,daxiao,num)
#     print(sql)
#     cursor.execute(sql)
#     db.commit()
#
# def update_win_daxiao(num,win_daxiao):
#     sql = "update shijiebei t set win_daxiao=%f" \
#           " where t.id='%s'" % (win_daxiao,num)
#     print(sql)
#     cursor.execute(sql)
#     db.commit()

if __name__ == '__main__':
    url_list = get_url_list()
    page = 1
    count = 0
    for url in url_list:
        print(url)
        page,count = game_list.get_game_list(url,page,count)
    #     #insert(result)
    #     for item in result:
    #         #print(item[0],item[1],item[2],item[3],item[4],"=======goal======",str(int(item[5][0])+int(item[5][2])))
    #         #ouzhi = zhishu.get_ouzhi('http://odds.500.com/fenxi/ouzhi-' + item[0] + '.shtml')
    #         #yazhi = zhishu.get_yazhi('http://odds.500.com/fenxi/yazhi-' + item[0] + '.shtml')
    #         daxiao = zhishu.get_daxiao('http://odds.500.com/fenxi/daxiao-' + item[0] + '.shtml')
    #         #print(int(item[5][0])+int(item[5][2]),daxiao[1][1])
    #         win_daxiao = tongji.tongji_daxiao(int(item[5][0])+int(item[5][2]),str(daxiao[1][1]).replace('↑','').replace('↓',''))
    #         #update(item[0], ouzhi, yazhi, daxiao)
    #         update_win_daxiao(item[0],win_daxiao)
    #         #print(win_daxiao)
    # db.close()

