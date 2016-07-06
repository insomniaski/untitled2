# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup




html_sec = requests.get("https://avmo.pw/cn/star/2cj").content
soup_sec = BeautifulSoup(html_sec, "lxml")
link_sec = soup_sec.find(id="waterfall")
print link_sec
for i in range(30):    #一页上显示30部影片
    if link_sec is not None:
        link_sec = link_sec.find_next("a", "movie-box")
        print(link_sec.get('href'))
        # 输出影片链接
        print(link_sec.find_next("date").string)
        # 输出番号
        print(link_sec.find_next("date").string)
        # 输出日期