import yagmail
import getpass
import requests
from pyquery import PyQuery as pq
from mymodule import stats_word as mk
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
doc=pq(response.text)
content = doc('#js_content').text()
try:#通过try...except捕获异常
    result=mk.stats_text_ch(content,100)
    sender = input('请输入发件人邮箱:')
    password = getpass.getpass('请输入发件人邮箱的授权码:')
    recipients = input('请输入收件人邮箱:')
    title = input('Please input the title:')
    yag = yagmail.SMTP(sender,password,'smtp.163.com')
    yag.send(to=recipients,subject=title,contents=str(result))
except ValueError as e:
    print(e)


