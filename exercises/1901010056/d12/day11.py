# 安装第三方库  requests ,yagmail,pyquery
# request  获取网页内容
# yagmail  发送邮件
# pyquery  获取text
import requests                         #输入requests网络请求库
import yagmail
import getpass
from pyquery import PyQuery as py
import stats_word11 as sw


    
# Import the content from website of "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA" 

r = requests.get('https://mp.weixin.qq.com/s?__biz=MzU2NDMzNTc4Mg==&mid=2247485976&idx=1&sn=1d3d14f9ec73d1555bb68e5701d8debb&chksm=fc4dcfd1cb3a46c77d9faf73e87bef2758262134e03b5c93054cf195fcceb9a0d2e6a5a8bf26&scene=0&xtrack=1#rd ')


web_text =r.text#使用变量web_text保护网页文本数据(这时会保存很多js代码以及其他function的代码,并不是里面所有的东西是我们需要的)
print(r.text)

# Extract the content from the source code
#提取微信公众号正文代码
document =py(web_text)
content = document('#js_content').text()

print('content =', content)
 

# Leverage function of 'stats_text' to identify the top 100 frequent words 
result = sw.stats_text_cn(content,100)
result=str(result)
print(result,str)#显示数据




sender = input("请输入您的发件人邮箱")
password =  getpass.getpass("输入发件人邮箱授权码")

yagmail.register(sender, password)

yag =yagmail.SMTP(sender,password,host='smtp.qq.com')
yag.send('malin199701@dingtalk.com', '自学训练营学习1群DAY11 pony6666', result)
print("发送成功")

'''
countlist_str = ''.join(str(i) for i in countlist)
print(countlist_str)

# Use getpass to enter the email address related information
import getpass
sender = input('2863727215@qq.com')    ##'Enter the email address of sender:'
password = getpass.getpass('gtwcugfmkfoaddbi') ##'Enter the password of the email from sender:'
recipients = input('malin199701@dingtalk.com') ##'Enter the email address of the reciever:'


# Leverage yagmail to send out emai
import yagmail
yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com') 
yag.send(recipients, '自学训练营学习1群DAY11 pony6666', countlist_str)    ###recipients是收件人的意思
'''
