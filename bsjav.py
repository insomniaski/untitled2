# !/usr/bin/env python
# -*- coding: utf-8 -*-
import  requests

# proxies = {
#         'http': 'http://183.237.18.56:9797',
#         'https': 'http://183.237.18.56:9797',
# }


from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Pass@word',
                             db='clctdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


i=1
k=1

def secondary_grab(url):
    #print url
    #html_sec=requests.get(url,proxies=proxies).content
    html_sec=requests.get(url).content
    soup_sec=BeautifulSoup(html_sec,"lxml")
    link_sec=soup_sec.find(id="waterfall")
    #print link_sec
    for i in range(30):
        if link_sec is not None:
            link_sec=link_sec.find_next("a","movie-box")
            print(link_sec.get('href'))
            #输出影片链接
            print(link_sec.find_next("date").string)
            #输出番号



while (k<5):
        url = "https://avmo.pw/cn/actresses/page/"
        print k
        #输出所在的页码
        url+=str(k)
        print url
        #html = requests.get(url,proxies=proxies).content
        html = requests.get(url).content
        #requests.close()
        soup = BeautifulSoup(html,"lxml")
        #tag=soup.span
        #print soup.find_all('span')
        link=soup.find(id="waterfall")
        #print link
        for i in  range(50):
            if link is not None:
                link=link.find_next("a")
                #print link.get('title')
                url2= link.get('href')
                print url2
                link=link.find_next("span")
                print link.string
                sql = "INSERT INTO actor(NAME,link,page,birth) VALUES (%s,%s,%s,%s)"
                connection.cursor().execute(sql, (link.string,url2,k,0))
                connection.commit()
                #secondary_grab(url2)
        k+=1

