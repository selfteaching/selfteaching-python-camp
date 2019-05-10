import requests

import pyquery

from pyquery import PyQuery

from stats_word import stats_text

import getpass

import yagmail



r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# 抓取网页



document = PyQuery(r.text)

content = document('#js_content').text()

#提取公众号正文，否则是大堆网页编码



r_list = stats_word.stats_text_cn(content,100)

r_str = str(r_list) #转换成str类型



'''
import pyodbc
conn = pyodbc.connect('DRIVER=MySQL ODBC 5.1 driver;SERVER=localhost;DATABASE=spt;UID=who;PWD=testest') 

csr = conn.cursor()  
csr.close()
conn.close()    #<--- Close the connection



user = input('2863727215@qq.com ') #邮箱账号

password = getpass.getpass('gtwcugfmkhoaddbi') #输入邮箱开通的smtp服务授权码

recipient = input('pythoncamp@163.com')

smtp = "smtp.qq.com" #服务器地址



yag = yagmail.SMTP(user,password,smtp)

yag.send(recipient,'自学训练营学1群DAY11 pony6666',r_str)
'''