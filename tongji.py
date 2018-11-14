import pymysql

import numpy as np
import pandas as pd
from scipy import stats,integrate
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



import seaborn as sns
sns.set(color_codes=True)

def tongji(zhu,ke,pankou):
    if pankou == '平手':
        if zhu - ke >= 0:
            return 1
        if zhu - ke == -1:
            return 0
        if zhu - ke < -1:
            return -1

    if pankou == '平手/半球':
        if zhu - ke >= 0:
            return 1
        if zhu - ke == -1:
            return -0.5
        if zhu - ke < -1:
            return -1

    if pankou == '半球':
        if zhu - ke >= 0:
            return 1
        if zhu - ke < 0:
            return -1

    if pankou == '半球/一球':
        if zhu - ke >= 1:
            return 1
        if zhu - ke == 0:
            return 0.5
        if zhu - ke < 0:
            return -1

    if pankou == '一球':
        if zhu - ke >= 1:
            return 1
        if zhu - ke == 0:
            return 0
        if zhu - ke < 0:
            return -1

    if pankou == '一球/球半':
        if zhu - ke >= 1:
            return 1
        if zhu - ke == 0:
            return -0.5
        if zhu - ke < 0:
            return -1

    if pankou == '球半':
        if zhu - ke >= 1:
            return 1
        if zhu - ke < 1:
            return -1

    if pankou == '球半/两球':
        if zhu - ke >= 2:
            return 1
        if zhu - ke == 1:
            return 0.5
        if zhu - ke < 1:
            return -1

    if pankou == '受平手/半球':
        if ke - zhu >= 0:
            return 1
        if ke - zhu == -1:
            return -0.5
        if ke - zhu < -1:
            return -1

    if pankou == '受半球':
        if ke - zhu >= 0:
            return 1
        if ke - zhu < 0:
            return -1

    if pankou == '受半球/一球':
        if ke - zhu >= 1:
            return 1
        if ke - zhu == 0:
            return 0.5
        if ke - zhu < 0:
            return -1

    if pankou == '受一球':
        if ke - zhu >= 1:
            return 1
        if ke - zhu == 0:
            return 0
        if ke - zhu < 0:
            return -1

    if pankou == '受一球/球半':
        if ke - zhu >= 1:
            return 1
        if ke - zhu == 0:
            return -0.5
        if ke - zhu < 0:
            return -1

    if pankou == '受球半':
        if ke - zhu >= 1:
            return 1
        if ke - zhu < 1:
            return -1

    if pankou == '受球半/两球':
        if ke - zhu >= 2:
            return 1
        if ke - zhu == 1:
            return 0.5
        if ke - zhu < 1:
            return -1


def update_time(db,coursor):
    sql = "select id,first_goal_time,win from gunqiu where first_goal_time<=45 and game_name='葡超'"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print("aaa")


def first_goal_time_relation(db,cursor):
    sql = "select first_goal_time,win from gunqiu t where t.pankou not like '受%' and t.first_goal_time <= 45 and t.game_name='巴甲'"
    cursor.execute(sql)
    list = []
    results = cursor.fetchall()
    for row in results:
        list.append([row[0],row[1]])
    # 关闭数据库连接
    db.close()
    x = np.array(list)
    sns.kdeplot(x, shade=True)

    max_win = 0
    time_max_win = 0
    print(list)
    winType = ''
    for time in range(46):
        win = 0
        win12 = 0
        win21 = 0
        for row in list:
            if int(row[0]) <= time:
                win12 += float(row[1])
            else:
                win12 -= float(row[1])

            if int(row[0]) <= time:
                win21 -= float(row[1])
            else:
                win21 += float(row[1])
        win = max(win12,win21)
        if max_win <= win:
            if win12 >= 0:
                winType = '12'
            else:
                winType = '21'
            time_max_win = time
        max_win = max(max_win,win)

    print(len(list),time_max_win,max_win,winType,max_win/len(list))
    plt.show()

def max_plan(date,game_name,pankou):
    sql = ""
    if pankou[0] == '受':
        sql = "select first_goal_time,win from gunqiu t where t.date >= "+str(date-1-10000)+" and t.date<" + str(date - 1) + " and t.pankou like '受%' and t.first_goal_time <= 45 and t.game_name='"+game_name+"'"
    else:
        sql = "select first_goal_time,win from gunqiu t where t.date >= "+str(date-1-10000)+" and t.date<" + str(date - 1) + " and t.pankou not like '受%' and t.first_goal_time <= 45 and t.game_name='"+game_name+"'"
    cursor.execute(sql)
    list = []
    results = cursor.fetchall()
    for row in results:
        list.append([row[0],row[1]])
    x = np.array(list)
    # sns.kdeplot(x, shade=True)

    max_win = 0
    time_max_win = 0
    # print(list)
    winType = ''
    for time in range(46):
        win = 0
        win12 = 0
        win21 = 0
        for row in list:
            if int(row[0]) <= time:
                win12 += float(row[1])
            else:
                win12 -= float(row[1])

            if int(row[0]) <= time:
                win21 -= float(row[1])
            else:
                win21 += float(row[1])
        win = max(win12,win21)
        if max_win <= win:
            if win12 >= 0:
                winType = '12'
            else:
                winType = '21'
            time_max_win = time
        max_win = max(max_win,win)

    # print(len(list),time_max_win,max_win,winType,max_win/len(list))
    if winType == "12":
        print(str(time_max_win),"分钟前建议正手买入")
        print(str(time_max_win),"分钟后建议反手买入")
    if winType == "21":
        print(str(time_max_win),"分钟前建议反手买入")
        print(str(time_max_win),"分钟后建议正手买入")
    return time_max_win,winType
    #plt.show()

def win_oneday(date):
    sql = "select t.jingcai_id,t.win,t.first_goal_time,t.date,t.game_name,t.pankou from gunqiu t where t.first_goal_time <= 45 and t.date="+str(date)+" order by jingcai_id"
    cursor.execute(sql)
    # list = []
    results = cursor.fetchall()
    print("共" + str(len(results)) + "条记录")
    res = []
    for row in results:
        print(row[0],row[2],row[1])
        time_max_win,winType = max_plan(int(row[3]),row[4],row[5])
        if winType == '12':
            if int(row[2]) <= time_max_win:
                res.append(float(row[1]))
                print("====================[" + str(row[1]) + "]=======================")
            else:
                res.append(float(row[1])*(-1))
                print("====================[" + str(float(row[1])*(-1)) + "]=======================")
        if winType == '21':
            if int(row[2]) <= time_max_win:
                res.append(float(row[1])*(-1))
                print("====================[" + str(float(row[1])*(-1)) + "]=======================")
            else:
                res.append(float(row[1]))
                print("====================[" + str(row[1]) + "]=======================")
    print(len(res),res,np.sum(res))

if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "gunxifacai", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        first_goal_time_relation(db,cursor)
        #win_oneday(20181104)
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()



