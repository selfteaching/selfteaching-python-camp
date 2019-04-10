import re
import sys
import jieba
import getpass
import yagmail
from mymodule import stats_word
#import json
#with open('tang300.json','r',encoding='UTF-8') as f:
   # text=f.read()

#print(stats_word.stats_text_cn(text, 20))
import requests
from pyquery import PyQuery
from mymodule import stats_word


response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
content = document('#js_content').text()
print(stats_word.stats_text(content,100))

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')
