import urllib
import urllib2


values = {}
values['Accept-Language'] = "zh-CN,zh;q=0.8"
values['Accept']="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
values['User-Agent']="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
data = urllib.urlencode(values)
request = urllib2.Request("http://91.3p7.us/v.php?next=watch&page=1",data)
response=urllib2.urlopen(request)
print response.read()