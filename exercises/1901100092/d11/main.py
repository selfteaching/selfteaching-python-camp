from mymodule import stats_word
from pyquery import PyQuery
import requests
import getpass
import yagmail

def load_file():

    response = requests.get(url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

    document = PyQuery(response.text)
    content = document('#js_content').text()
    return content

#text=1                  #验证参数检查功能是否生效
try:
    i = stats_word.stats_text_cn(load_file())
    print(i)
except ValueError:
    print('stats_text参数应为字符串类型')

sender = input('输入发件人邮箱：')
password_1 = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')

yag = yagmail.SMTP(user = sender,password = password_1,host = 'smtp.qq.com')
yag.send(to = recipients,subject = "【1901100092】自学训练营学习15群DAY11 Yui",contents = str(i))
