# !/usr/bin/env python
# -*- coding: utf-8 -*-
import  requests
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
i=1

k=1

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Pass@word',
                             db='clctdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


while (k<20):
        url = "http://www.qschou.com/index/project/projects/"
        # print k
        url+=str(k)
        print url
        html = requests.get(url).content

        soup = BeautifulSoup(html,"lxml")
        tag=soup.span
        #print soup.find_all('span')
        link=soup.find(id="tab-1")
        #print link
        for i in  range(6):
            if link is not None:
                link=link.find_next("a")
                print link.get('title')
                url2= "http://www.qschou.com"+link.get('href')
                print url2
                sql = "INSERT INTO `demotable` (`id`, `name`) VALUES (%s,%s)"
                connection.cursor().execute(sql,(url2,link.get('title')))
                connection.commit()
                html2=requests.get(url2).content
                soup2=BeautifulSoup(html2,"lxml")
                link2=soup2.find('div',"qsc-project-status_detail clearfix")#二级页面抓取
                #print link2
                link3=link2.find_all("strong")
                for elem in link3:
                    print elem.get_text()
                link4=soup2.find("h4")
                print link4.find_next("strong").get_text()
#
                # link=link.find_next("span")
                # print link.string
                #
                # link = link.find_previous("a")
                # print link.get('href')

        # for link in soup.find_all("span",["title"]):
        #         print i
        #         print link.string
        #         i+=1
        k+=1

