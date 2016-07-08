# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup




html_sec = requests.get("https://avmo.pw/cn/star/2cj").content
soup_sec = BeautifulSoup(html_sec, "lxml")
link_sec = soup_sec.find(id="waterfall")
#print link_sec
for i in range(30):    #一页上显示30部影片
    if link_sec is not None:
        link_sec = link_sec.find_next("a", "movie-box")
        url_movie=(link_sec.get('href'))
        print url_movie#输出影片链接

        html_movie=requests.get(url_movie).content
        soup_movie=BeautifulSoup(html_movie,"lxml")
        #print soup_movie
        link=soup_movie.find('div',"col-md-3 info")
        link=link.find_all("span","genre")
        #print link
        description=""
        for link_elem in link:
            description+=link_elem.get_text()
        print description
        #print(link_sec.find_next("span").get_text())
        # 输出番号
        print(link_sec.find_next("date").string)
        # 输出日期