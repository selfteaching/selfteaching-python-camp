
# coding: utf-8

# In[18]:


import sys
sys.path.append(r'C:\Users\hx\Documents\GitHub\selfteaching-python-camp\exercises\1901050037\d11\mymodule')
import stats_word
from collections import Counter
import re
import json
import jieba
import requests
import getpass
import yagmail
from pyquery import PyQuery 
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content_input = document('#js_content').text()

result_str = str(stats_word.stats_text(content_input,100))
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人密码（可复制粘贴）：')
recipients=input('输入收件人邮箱:')
smtp = 'smtp.qq.com'
yag = yagmail.SMTP(user=sender,password=password,host=smtp)
yag.send(to=recipients,subject='自学训练营学习4群Day11+hx137461197',contents=result_str)
print('发送成功')


