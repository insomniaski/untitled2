# !/usr/bin/env python
import  requests

# proxies = {
#         'http': 'http://183.237.18.56:9797',
#         'https': 'http://183.237.18.56:9797',
# }


from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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
            print(link_sec.find_next("date").string)



while (k<2):
        url = "https://avmo.pw/cn/actresses/page/"
        # print k
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
                #print link.string
                secondary_grab(url2)
        k+=1

