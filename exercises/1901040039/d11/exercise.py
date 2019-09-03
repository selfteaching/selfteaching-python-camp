import requests
import pyquery
from pyquery import PyQuery
import mymodule.stats_word
import getpass
import yagmail


r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
#抓取网页

document = PyQuery(r.text)
content = document('#js_content').text()
#提取公众号正文，否则是大堆网页编码


r_list = mymodule.stats_word.stats_text_cn(content,100)
r_str = str(r_list) #转换成str类型


user = input('请输入你的邮箱：')#邮箱账号
password = getpass.getpass('清输入发件人邮箱密码（smpt授权码):') #输入邮箱开通的smtp服务授权码
recipient = input('请输入收件人邮箱：')
smtp = "smtp.qq.com"#服务器地址


yag = yagmail.SMTP(user,password,smtp)
yag.send(recipient,'自学训练营3群DAY11 hanwuji1',r_str)
 
