import getpass
sender=input('fajian:')
password=getpass.getpass('mima:')
recipients=input('shoujian:')
import sys
import json
import os
import jieba
import yagmail
from collections import Counter
import requests
r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
sys.path.append('E:\self-teaching\selfteaching-python-camp\exercises\1901100167\d11\mymodule')
from mymodule import stats_word
from pyquery import PyQuery
document=PyQuery(r.text)
content=document('#js_content').text()
a=stats_word.stats_text_cn(content)
b=(''.join('%s:%s\n')%id for id in a)
yag=yagmail.SMTP(user=sender,password=password,host='smtp.163.com')
content1=str(a)
yag.send(to=recipients,subject='自学训练营18群 1901100167 Day11 comevback',contents=content1)