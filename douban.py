# -*- coding: utf-8 -*-

import requests
# import scrapy
import urllibtest
import re
import random
from time import sleep

url = "https://movie.douban.com/top250?start="
#while (1):

response = requests.get(url)
content = response.content
#print content
pattern=re.compile(r'<span class="title">(.*?)</span>')
result=re.findall(pattern,content)
print '结果:'
print result
i=0
for item in result:
    print i
    print item
    i+=1