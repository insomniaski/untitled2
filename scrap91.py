# !/usr/bin/env python
import  requests

from bs4 import BeautifulSoup


i=1
k=1


while (k<2):
        url = "http://email.91dizhi.at.gmail.com.8h5.space/v.php"
        payload={'next':'watch','page':'1'}
        headers ={'Accept-Encoding': '','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        data={'session_language':'cnCN'}
        #headers ={'Accept-Encoding': '','Accept-Language':'zh-CN,zh;q=0.8'}
        # print k
        #url+=str(k)
        #print url
        #html = requests.get(url,proxies=proxies).content
        s = requests.session()
        html = s.post(url,params=payload,headers=headers,data=data).content
        #requests.close()
        soup = BeautifulSoup(html,"lxml")
        #tag=soup.span
        #print soup.find_all('span')
        link=soup.find(id="videobox")
        #print link
        for i in  range(20):
            if link is not None:
                link=link.find_next('div','listchannel')
                #print link
                link=link.find_next('a')
                #print link
                print link.get("href")
                link=link.find_next('img')
                print link.get("title")



        k+=1

