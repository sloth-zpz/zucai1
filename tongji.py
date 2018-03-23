import pymysql

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


# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "", "gunxifacai",charset="utf8")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 查询语句
# sql = "select * from gunqiu"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     aaa = 0
#     for row in results:
#         zhu = row[3]
#         ke = row[4]
#         pankou = row[5]
#         aaa += tongji(zhu,ke,pankou)
#         # 打印结果
#         print(tongji(zhu,ke,pankou))
#     print(aaa)
# except:
#     print("Error: unable to fetch data")
#
# # 关闭数据库连接
# db.close()


