import getpass
import yagmail
#sender = input('woaxiangxiang@foxmail.com')
#password = getpass.getpass('qqmimaasus17715') 
#recipients = input('184094775@qq.com')

yag = yagmail.SMTP(user = "184094775@qq.com", password = "wdbqzdfthegibhcb", host='smtp.qq.com')

# 邮箱正文
contents = ['send you picture！']

# 发送邮件
yag.send('pythoncamp@163.com', '打招呼！',contents)