import getpass
sender = input('输⼊发件⼈邮箱:')
password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):')
recipients = input('输⼊收件⼈邮箱:')

from  mymodule import stats_word

import requests
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',auth = ('user','pass'))
# print(r)
r.status_code
# 提取微信公众号正⽂伪代码示例
from pyquery import PyQuery
document = PyQuery(r.text)
content = document('#js_content').text()
# print(content)

x = stats_word.stats_text_cn(content)
# s = " ".join (x)
values = ','.join(str(v) for v in x)
print (values)

import yagmail
# yag = yagmail.SMTP(sender,password,'yaowenxin0915@gmail.com')   1311557847@qq.com pythoncamp@163.com
# 这个要用对应邮箱的服务器后缀，我猜gmail或许是这个？
# yag = yagmail.SMTP(sender,password,'smtp.gmail.com')
yag = yagmail.SMTP(sender,password,'smtp.qq.com')

to = recipients   # 上面有收件人的
subject = '【1901100081】⾃学训练营学习15群 DAY11 yaodadada'
body = values
yag.send(to = to,subject = subject, contents = body )