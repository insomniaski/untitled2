# -*- coding: utf-8 -*-

import requests
# import scrapy
import urllib
import re
import random
import HTMLParser
from time import sleep

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


url = "https://movie.douban.com/top250?start="
#while (1):

response = requests.get(url)
print response.encoding
content = response.content

#content.encoding='utf-8'

html_parser = HTMLParser.HTMLParser()
txt = html_parser.unescape(content)
html_parser.feed(content)


print txt

