# !/usr/bin/env python


import requests
# import scrapy
import urllib
import re
import random
from time import sleep

url = "http://www.heibanke.com/lesson/crawler_ex00/"
while (1):

    response = requests.get(url)
    content = response.content

    #print content
    # pattern = re.compile(r'<h3>(.*)</h3>')
    pattern = re.compile(r'<h3>(.*)[0-9](.*)</h3>')
    result = re.search(pattern, content)

    string = result.group()
    string = string[4:-5]
    print re.findall(r'[0-9]{5}',string)

    #print string.find('/d{5}')
    url += string
