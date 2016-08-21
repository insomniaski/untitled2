# -*- coding: utf-8 -*-
import  requests

base_usr="http://jp.atracking.appflood.com"

click_url = base_usr+"/transaction/post_click?offer_id=317&aff_id=129&aff_sub6=abcd1234"
click_res = requests.post(click_url,allow_redirects=False).content#发起点击
print click_res
position=click_res.index("transaction_id")

tran_id= click_res[position+15:position+49]

conv_url=base_usr+"/transaction/post_conversion?transaction_id="+tran_id
print conv_url
conv_res=requests.post(conv_url,allow_redirects=False).content#确认转化

print conv_res
if conv_res =='"1"':
    print 'sussess'



#print tran_id