from new import http_to_char,tongji,oupei
from lxml import etree


def get_game_list(url,page,count):
    content = http_to_char.get_content_by_url(url)
    root = etree.HTML(content)
    table_game = root.xpath('//tr[@yy]')
    for data_game in table_game:
        if data_game.xpath('./td/span[@class="red"]/text()')[0] == '完':
            game_id = str(data_game.xpath('./@id')[0][1:])
            num_zhu = int(data_game.xpath('./td/div[@class="pk"]/a/text()')[0])
            pankou = str(data_game.xpath('./td/div[@class="pk"]/a/text()')[1])
            num_ke = int(data_game.xpath('./td/div[@class="pk"]/a/text()')[2])

            # 欧盘输赢情况
            out = tongji.tongji_yapan(num_zhu,num_ke,pankou)

            result_list = oupei.get_oupei(game_id)
            result_list.append(out)

            if ((count != 0) & (count % 50 == 0)):
                page = page + 1
            with open("oupei" + str(page) + ".csv", 'a', encoding="utf-8") as f:
                f.writelines(','.join(str(i) for i in result_list))
                f.write('\n')

            count = count + 1
    return page,count




