#-*- coding:utf-8 -*-

from urllib import request
from lxml import etree

url="http://odds.500.com/fenxi/yazhi-723209.shtml"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

page = request.Request(url=url,headers=headers)
page_info = request.urlopen(page).read().decode("gbk", 'ignore').encode('utf8')
print(u""+page_info)
root = etree.HTML(page_info)
