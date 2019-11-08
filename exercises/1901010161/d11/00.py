import requests
import getpass
import yagmail
from pyquery import PyQuery as py
from mymodule import stats_word

reponse = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')   # 网页请求
web_text = reponse.text    # 保存更多网页文本数据
document = py(web_text)
content = document('#js_content').text()
print('content=', content)

w_list = stats_word.stats_text_cn(content, 100)
w_list = str(w_list)
print(w_list)

sender = input("请输入发件人邮箱:")
password = getpass.getpass("输入发件人邮箱授权码:")

yagmail.register(sender, password)

yag = yagmail.SMTP(sender, password, host='smtp.qq.com')
yag.send('pythoncamp@163.com', '【1901010161】自学训练营学习2群DAY11 Zezhou-Sun', w_list)
print("发送成功")

'''
countlist_str = ''.join(str(i) for i in countlist)
print(countlist_str)
# Use getpass to enter the email address related information
import getpass
sender = input('894101858@qq.com')    ##'Enter the email address of sender:'
password = getpass.getpass('kdkrtqtbtazubdef') ##'Enter the password of the email from sender:'
recipients = input('pythoncamp@163.com') ##'Enter the email address of the reciever:'
# Leverage yagmail to send out emai
import yagmail
yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com')
yag.send(recipients, '【1901010161】自学训练营学习2群DAY11 Zezhou-Sun', countlist_str)
'''
