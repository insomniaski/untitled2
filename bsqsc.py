# !/usr/bin/env python
import  requests
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
i=1

k=1
while (k<35):
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

                link=link.find_next("a")
                print link.get('title')
                print "http://www.qschou.com"+link.get('href')


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

