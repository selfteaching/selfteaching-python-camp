from pyquery import PyQuery
from mymodule import d11_stats_word
import yagmail
import getpass
import requests



# 获取公众号文件
payload = dict(key1='value1', key2='value2')
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',data=payload)


# 提取公众号正文

document = PyQuery(response.text)
content = document('#js_content').text()

Slist = d11_stats_word.stats_text(content)

S1 = " ".join(str(i) for i in Slist)

sender = input('输入发件人邮箱:' '176665323@qq.com')
password = getpass.getpass('输入发件人邮箱密码:' 'fxlsojlzcddgbgjc')
recipients = input('输入收件人邮箱:' 'pythoncamp@163.com')
host = "smtp.qq.com"

yag = yagmail.SMTP(sender,password,"smtp.qq.com")

yag.send(recipients,'19100105 liwanlsl',S1)    

