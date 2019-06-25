
from mymodule import stats_word
import json
from os import path    
from collections import Counter
import jieba
import yagmail
import requests
from pyquery import PyQuery
import getpass

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
documenmt = PyQuery(response.text)
content = documenmt('#js_content').text()

string = str(stats_word.stats_text_cn(content, 100))

yag = yagmail.SMTP()
yag.send('pythoncamp@163.com', '1901050119 Galaxy1227', string)