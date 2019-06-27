
from mymodule import stats_word
import json
from os import path    
from collections import Counter
import jieba
import yagmail
import requests
from pyquery import PyQuery
import getpass

def get_text():
    response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(response.text)
    return document('#js_content').text()


content = get_text()
result = stats_word.stats_text_cn(content, 100)

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')

yag = yagmail.SMTP(sender, password, 'smtp.qq.com')
yag.send('pythoncamp@163.com', '1901050119 Galaxy1227', str(result))