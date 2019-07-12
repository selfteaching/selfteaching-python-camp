
# encoding=utf-8
import jieba
import yagmail
import requests
from pyquery import PyQuery
from collections import Counter

from mymodule import stats_word
import getpass
import logging
# 提取公众号文章里的正文内容并统计词频前100的词汇
path = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
def get_article(path):
    # 链接获取的内容
    response = requests.get(path, auth=('user', 'pass'))
    # 提取正文
    document = PyQuery(response.text) 
    # 返回正文字符串
    return  document('#js_content').text()
word_list =  stats_word.stats_text_cn(get_article(path),100)
# word _list = ''.join(word_list)
words = []
for item in word_list:
    words.append(item[0])
words = ','.join(words)    

'''
recipients ="1963721578@qq.com"
"pythoncamp@163.com"
'''
try:
    sender = "danagcong@163.com"
    # password = getpass.getpass('dangcong1993') 
    psd_key = "dangcong1993"
    host = 'smtp.163.com'
    recipients = ["pythoncamp@163.com",sender]

    mail = yagmail.SMTP(user = sender,password = psd_key ,host = host)
    mail.send(subject = '自学营009期01班 JiJun-1993',contents = words)
    print("sdfsdaffsf")
except:
    print("登录失败")