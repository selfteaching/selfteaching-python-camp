import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from mymodule import stats_word
from os import path
import json
import re
import logging

import requests
from pyquery import PyQuery
import yagmail

import getpass
sender = input('输⼊入发件⼈人邮箱:')
password = getpass.getpass('输⼊入发件⼈人邮箱密码(可复制粘贴):')
recipients = input('输⼊入收件⼈人邮箱:')

r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(r.text)
content = document('#js_content').text()


ll_word = []
ll_num  = []
for ll in wx_list:
    ll_word.append(ll[0])
    ll_num.append(ll[1])
    
print(ll_word)
print(ll_num)
        
        
        

#wx_str =''

#for word in wx_list:
#   wx_str = wx_str + str(word)

#yagmail.SMTP('sender','password').send('pythoncamp@163.com','[1901100303]自学训练营学习20群 day11 yuanweiyu',wx_str)








