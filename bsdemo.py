# !/usr/bin/env python
import  requests
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
i=1

k=0
while (k<10):
        url = "https://movie.douban.com/top250?start="
        # print k
        url+=str(25*k)
        print url
        html = requests.get(url).content

        soup = BeautifulSoup(html,"lxml")
        tag=soup.span
        #print soup.find_all('span')
        link=soup.find(("h1"))
        print link
        for i in  range(25):

                link=link.find_next("em")
                print link.string

                link=link.find_next("span")
                print link.string

                link = link.find_previous("a")
                print link.get('href')

        # for link in soup.find_all("span",["title"]):
        #         print i
        #         print link.string
        #         i+=1
        k+=1

