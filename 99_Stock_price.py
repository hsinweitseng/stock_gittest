# -*- coding: utf-8 -*-

import datetime
import ystockquote
import Python_sms
import time

Stock_list = 'GOOG','TSLA','WDC','NUGT','DUST'
print(Stock_list)
for i in Stock_list:
    stock_price = ystockquote.get_price(i)
    print(stock_price)
    print('Sending text to phone now')
    Python_sms.Send_SMS(i+' '+stock_price)
    print('finish sending',i+' '+stock_price)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d %H %M')
#st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d %H%M%S')
print(str(st))
current_time = str(st)
print(current_time)
Python_sms.Send_SMS(current_time)
Python_sms.Send_SMS('嘸蝦米輸入法')
Chinese_text = '嘸蝦米輸入法'
Python_sms.Send_SMS(Chinese_text)
