
# -*- coding: utf-8 -*-
import HTMLParser


class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)

    def handle_startendtag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            # 判断标签<a>的属性
            for name, value in attrs:

                    print value



a = '<a href="https://movie.douban.com/subject/6786002/" class=""><span class="title">触不可及</span><span class="title"> / Intouchables</span><span class="other"> / 闪亮人生(港)  /  逆转人生(台)</span></a>'

my = MyParser()
# 传入要分析的数据，是html的。
my.feed(a)