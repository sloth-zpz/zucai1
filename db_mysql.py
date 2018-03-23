#！/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","","mybatis-test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM classroom"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        # 打印结果
        print("fname=%s,lname=%s" % \
              (fname, lname))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()