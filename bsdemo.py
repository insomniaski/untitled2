# !/usr/bin/env python
import  requests
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

html = requests.get("https://movie.douban.com/top250?start=").content

soup = BeautifulSoup(html,"lxml")

for link in soup.find_all("span","title"):

        print link.string#yes

