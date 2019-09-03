import requests
from pyquery import PyQuery
import stats_word
import getpass
import yagmail
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(r.text)
content = document('#js_content').text()
r_list = stats_word.stats_text_cn(content, 100)
r_str = str(r_list)
print(r_str)

user = input('请输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipient = input('请输入收件人邮箱：')
smtp = "smtp.163.com"
yag = yagmail.SMTP(user,password,smtp)
yag.send(recipient,'自学训练营2群 DAY11 zhangshilina',r_str)
