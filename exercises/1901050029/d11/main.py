# Filename : main.py
# author by : 张金磊

#import pandas as pd
import yagmail
import requests
import getpass
from mymodule import stats_word
from pyquery import PyQuery as py

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = py(response.text) 
content = document('#js_content').text()

text_1 = stats_word.stats_text_cn(content,100)



sender = input('请输入发件人邮箱：')
password = getpass.getpass('请输入发件人邮箱密码：')
recipients ='pythoncamp@163.com'      
host = 'smtp.qq.com'

yag = yagmail.SMTP(sender,password,host)
subject1 = '自学训练营学习4群 DAY11 JinleiReborn'
text_2= str(text_1)
yag.send(recipients,subject=subject1,contents=text_2)




        

 

