
#使用requests请求微信公众号文章的链接，获取返回结果（response）
import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

#将response.text，用pyquery提取正文
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()
#print(type(content))

#用stats_word中的stats_text对提取结果进行词频分析，结果转换成str
from mymodule import stats_word
str_con = str(content)
#print(type(str_con))
#print(str_con)
#print('字频最高的前100字统计结果： ', stats_word.stats_text_cn(str_con))
#现在的问题是换行符号也给统计进去了，暂未解决。正则表达没看懂也许有关系。
str_result = str(stats_word.stats_text_cn(str_con))
#print(str_result)

#登录邮箱发邮件 参考@slona-song同学的作业和issue#1057
import yagmail
import getpass

#sender = input('发件邮箱：')
sender = 'zhluchen@163.com'
password = getpass.getpass('邮箱授权密码:') #这里应该输入开通smtp的时候设置的授权密码，并非邮箱登录密码！！！
#recipients = input('收件邮箱')
recipients = 'pythoncamp@163.com'
sever = 'smtp.163.com'   #使用的服务器

yag = yagmail.SMTP(sender,password,host=sever) 
#contents = [str_result]
yag.send(to = recipients, subject = '19100303 Luchen1471', contents = str_result)    #给目标发邮件
yag.send(subject = '19100303 Luchen1471',contents = str_result)                      #给自己发邮件             

#发邮件也没有想象的那么简单啊
#自己收到邮件，庆祝撒花~~