import  re 
import  collections  
count = int()
#英文词频统计函数
def  stats_text_en(text,count):
    if type(text) == str :
            a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词
            newlist=a.split()                      #单词划分
            return(collections.Counter(newlist).most_common(count))  #输出英文单词频数统计结果
    else :
            raise ValueError ('type of argumengt is not str')


#中文词频统计函数
def  stats_text_cn(text,count):
    if type(text) == str : 
            p =  re.compile(r'[\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
            res = re.findall(p, text)   #取中文
            newcn=''.join(res)
            return(collections.Counter(newcn).most_common(count))  #输出中文词频统计结果
    else:
            raise ValueError ('type of argumengt is not str')


#分别调用stats_text_en、stats_text_cn，并合并输出词频统计结果
def  stats_text(text,count):
    if type(text)==str:
            return(stats_text_en(text)+stats_text_cn(text))  
    else:
            raise ValueError ('type of argumengt is not str')


with open(path,'r',encoding='UTF-8') as f:

import requests                         #输入requests网络请求库
from pyquery import PyQuery
from mymodule.stats_word11 import stats_word 
website ='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
 
# Import the content from website of "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA" 
response = requests.get(website,verify=False)
s = requests.session()
s.keep_alive = False
# Extract the content from the source code
#提取微信公众号正文代码
document = PyQuery(response.text) 
content = document('#js_content').text()
 
# Leverage function of 'stats_word' to identify the top 100 frequent words 
countlist = stats_word(content,100)
countlist_str = ''.join(str(i) for i in countlist)
print(countlist_str)

# Use getpass to enter the email address related information
import getpass
sender = input('2863727215@qq.com')    ##'Enter the email address of sender:'
password = getpass.getpass('2017xuelexue') ##'Enter the password of the email from sender:'
recipients = input('pythoncamp@163.com') ##'Enter the email address of the reciever:'
 
# Leverage yagmail to send out emai
import yagmail
yag = yagmail.SMTP(user=sender, password=password, host='smtp.weixin.qq.com') 
yag.send(recipients, '自学训练营学习1群DAY11 pony6666', countlist_str)    ###recipients是收件人的意思

import pyodbc
conn = pyodbc.connect('DRIVER=MySQL ODBC 5.1 driver;SERVER=localhost;DATABASE=spt;UID=who;PWD=testest') 

csr = conn.cursor()  
csr.close()
conn.close()     #<--- Close the connection


 