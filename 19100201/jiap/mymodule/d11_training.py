# -*- encoding: utf-8 -*-
import requests
from pyquery import PyQuery
import getpass
import stats_word
import yagmail

url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
response = requests.get(url)
document = PyQuery(response.text) 
content = document('#js_content').text()

string = ','.join(str(i) for i in stats_word.stats_text_cn(content))

sender = input('􏳁􏳂􏰥􏱖􏰾􏱮􏱯请输入发件人邮箱: ')
password = getpass.getpass('请输入发件邮箱密码􏳁􏳂􏰥􏱖􏰾􏱮􏱯􏲵􏲳:')
recipients = input('输入收件人邮箱: ')
contents = [string]


yag = yagmail.SMTP(user = sender, password = password, host='smtp.163.com')

yag.send(recipients, '19100201 jiap', contents)
print("Send successfully!")