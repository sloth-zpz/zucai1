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
    sql = "select first_goal_time,win from gunqiu where first_goal_time<=45 and date<=20180605 and date>=20170605"
    cursor.execute(sql)
    list = []
    results = cursor.fetchall()
    for row in results:
        list.append([row[0],row[1]])
    # 关闭数据库连接
    db.close()
    x = np.array(list)
    sns.kdeplot(x, shade=True)
    plt.show()
    print(len(list))

if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "gunxifacai", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        first_goal_time_relation(db,cursor)
    except:
        print("Error: unable to fetch data")




