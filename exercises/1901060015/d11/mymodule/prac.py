import yagmail
import getpass

yag = yagmail.SMTP(user= input('输入发件人邮箱：'),password= input('输入密码：'),host='smtp.163.com')

#邮件正文
contents ='hello my love'

#发送邮件
yag.send(to= input('收件人邮箱：'),subject= '测试',contents= [contents])
print('已发送邮件')