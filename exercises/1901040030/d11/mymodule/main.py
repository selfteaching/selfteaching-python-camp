import stats_word
import json
import requests
from pyquery import PyQuery
import yagmail
import getpass

#获取网页内容
response= requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA', auth=('user', 'pass'))
document = PyQuery(response.text)
content = document('#js_content').text()#获取文本
count=100  #限制输出元素的变量
try: 
    text_list= stats_word.stats_text(content,count) #调用统计汉字的函数
    text_list2=[] 
    for i in text_list: 
        text_list2.append(i[0]+':'+str(i[1])+';')#把text_list里面的元素处理成str存在text_list2里
    text_str=''.join(text_list2)#把列表转换成str
    print(text_str)
    
except ValueError as identifier: 
    print('请输入字符串',identifier) 



sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients = input('输入收件人邮箱：')
contents=text_str
subject='【自学训练营学习3群】Day11 wangzhenjia'

stmp='smtp.qq.com'
yag=yagmail.SMTP(sender,password,stmp)
yag.send(recipients,subject,contents)

