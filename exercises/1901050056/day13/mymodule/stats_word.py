from collections import Counter
from pyquery import PyQuery
import re
import jieba
import requests
import json
import yagmail
import getpass
import matplotlib.pyplot as plt
import numpy as np

def stats_text_en(text,count):
    if type(text)==str:
        edit_text = re.sub("[^A-Za-z]", " ", text)
        edit_text = edit_text.split()

    else:
        raise ValueError ('type of argumengt is not str')

    counter = Counter(edit_text).most_common(count)
    return counter#返回这个统计好的字典

# print('==============分割线===================')

def stats_text_cn(text,count):
    if type(text)==str:
        edit_text = re.compile(r'[\u4e00-\u9fa5]+')
        res = re.findall(edit_text,text)
        cnstr = ''.join(res)
    else:
        raise  ValueError ('type of argumengt is not str')

    after_jieba = jieba.cut(cnstr)
    tmp = []
    for i in after_jieba:
        if len(i)>1:
            tmp.append(i)

    counter = Counter(tmp).most_common(count)
    return counter#返回这个统计好的字典


def test_get_link():#抓取张小龙的演讲链接获取文本
    response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(response.text)
    content = document('#js_content').text()
    return content

def email(my_contents):#这是发邮件函数
    sender = input('输入发件人邮箱:')
    my_password = getpass.getpass('输入发件人邮箱密码(可复制粘贴):')
    recipients = input('输入收件人邮箱:')
    yag = yagmail.SMTP(sender,my_password,'smtp.qq.com')
    yag.send(recipients, '【1901050056】自学训练营学习4群 day11 lyxfree', my_contents)


def stats_text(text,count):#将统计中文和英文的两个函数做成一个函数
    if type(text)==str:
        s1=stats_text_en(text, count)
        s2=stats_text_cn(text, count)
        s3 = s1 + s2
        return s3
       
    else:
        raise ValueError ('type of argumengt is not str')
