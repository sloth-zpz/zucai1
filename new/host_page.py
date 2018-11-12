from new import http_to_char
from lxml import etree

def get_game_end(url):
    content = http_to_char.get_content_by_url(url)
    root = etree.HTML(content)
    table_game = root.xpath('//tr[@yy]')
    result = []
    for data_game in table_game:
        if data_game.xpath('./td/span[@class="red"]/text()')[0] == '完':
            num = data_game.xpath('./@id')[0][1:]
            duiwu = data_game.xpath('./@gy')[0]
            game = str(duiwu).split(',')
            game_name = game[0]
            changci = data_game.xpath('./td[3]/text()')[0]
            zhu_name = game[1]
            ke_name = game[2]
            num_zhu = data_game.xpath('./td/div[@class="pk"]/a/text()')[0]
            num_ke = data_game.xpath('./td/div[@class="pk"]/a/text()')[2]
            str_quan = str(num_zhu)+'-'+str(num_ke)
            str_ban = data_game.xpath('./td[9]/text()')[0]
            num_goal = int(num_zhu)+int(num_ke)

            first_goal_team = None
            firt_goal_time = None
            goal_decs = None
            if int(num_zhu)+int(num_ke) != 0:
                first_goal_team,firt_goal_time,goal_decs = goal_detail("http://live.500.com/detail.php?fid="+num+"&r=1")
            result.append((num,game_name,changci,zhu_name,ke_name,str_quan,str_ban,num_goal,first_goal_team,firt_goal_time,goal_decs))
    return result

def get_game(url):
    content = http_to_char.get_content_by_url(url)
    root = etree.HTML(content)
    table_game = root.xpath('//tr[@yy]')
    for data_game in table_game:
        if data_game.xpath('./td/span[@class="red"]/text()')[0] == 0:
            num = data_game.xpath('./@id')[0][1:]
            duiwu = data_game.xpath('./@gy')[0]
            game = str(duiwu).split(',')
            game_name = game[0]
            zhu_name = game[1]
            ke_name = game[2]
            num_zhu = data_game.xpath('./td/div[@class="pk"]/a/text()')[0]
            num_ke = data_game.xpath('./td/div[@class="pk"]/a/text()')[2]
            str_ban = data_game.xpath('./td[9]/text()')
            num_goal = int(num_zhu) + int(num_ke)


def goal_detail(url):
    content = http_to_char.get_content_by_url(url)
    root = etree.HTML(content)
    aa = root.xpath('//table[@class="mtable"]//tr')
    list=[]
    for data in aa:
        if len(data.xpath('./td/img[@src="/images/row/1.gif"]'))+len(data.xpath('./td/img[@src="/images/row/2.gif"]'))+len(data.xpath('./td/img[@src="/images/row/3.gif"]')) != 0:
            list.append(data)
    num_zhu = 0
    num_ke = 0
    str_goal = ""
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
    try:
        if list[0].xpath('./td/text()')[0] == '\xa0':
            return '客队',list[0].xpath('./td/text()')[2][:-1],str_goal
        else:
            if len(list[0].xpath('./td/text()')) == 3:
                return '主队',list[0].xpath('./td/text()')[0][:-1],str_goal
            else:
                return '主队',list[0].xpath('./td/text()')[1][:-1],str_goal
    except IndexError:
        return "",-1,""

