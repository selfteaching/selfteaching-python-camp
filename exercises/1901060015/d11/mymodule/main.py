import requests
from pyquery import PyQuery
import stats_word
import getpass
import yagmail

#用文章链接，获取返回结果
r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")


#提取正文
d=PyQuery(r.text)
c=d('#js_content').text().replace("，","").replace("。","").replace("\n","")

c1 = stats_word.stats_text_cn(c)
#转换为字符串
c2 =str(c1)


yag = yagmail.SMTP(user= input('输入发件人邮箱：'),password= input('输入密码：'),host='smtp.163.com')

#邮件正文
contents =c2

#发送邮件
yag.send(to= input('收件人邮箱：'),subject= '【1901060015】学训练营5群 DAY11 piaolong',contents= [contents])
print('已发送邮件')











