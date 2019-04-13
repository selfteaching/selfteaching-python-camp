import requests
import getpass
import yagmail
from pyquery import PyQuery
from mymodule import stats_word

# 设置邮箱
user = input('请输入你的邮箱:') #邮箱账号
password = getpass.getpass('请输入发件人邮箱密码(可复制粘贴)：') #邮箱开通smtp服务授权码
recipient = input('请输入收件人邮箱:')
smtp = "smtp.163.com" #服务器地址
# print(user,password,recipient)  #检查

# 发送邮件
yag = yagmail.SMTP(user,password,smtp)
yag.send(recipient,'19100101 sundyyang',day11_1)