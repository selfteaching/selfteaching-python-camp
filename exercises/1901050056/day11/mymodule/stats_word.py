from collections import Counter
from pyquery import PyQuery
import re
import jieba
import requests
import json
import yagmail
import getpass

def stats_text_en(text,count):
    if type(text)==str:
        edit_text = re.sub("[^A-Za-z]", " ", text)
        edit_text = edit_text.split()

    else:
        raise ValueError ('type of argumengt is not str')

    counter = Counter(edit_text).most_common(count)
    counter = dict(counter)
    #print(counter)
    for key in counter:#将数据按照格式化打印出来
        print("英文字符里这个：'{}'字符出现了{}次".format(key, counter[key]))

    a_dir = sorted(counter.items(),key=lambda x:x[1],reverse=True)
    #print(a_dir)
#上面这句话是将字典中的数据进行排序
    list2 = []
    for i in a_dir:#排序好之后遍历取出字符就好，数字就不要了
        list2.append(i[0])#取出符合条件的字符加入新的列表
    return list2#返回这个排序好之后的字符

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
    counter = dict(counter)
    for key in counter:#将数据按照格式化打印出来
        print("中文字符里这个：'{}'字符出现了{}次".format(key, counter[key]))

    a_dir = sorted(counter.items(), key=lambda x: x[1], reverse=True)
# 上面这句话是将字典中的数据进行排序
    list1 = []
    for i in a_dir:#排序好之后遍历取出字符就好，数字就不要了
        list1.append(i[0])#取出符合条件的字符加入新的列表
    return list1


def test_get_link():#抓取张小龙的演讲链接获取文本
    response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(response.text)
    content = document('#js_content').text()
    return content

def email(my_contents):
    sender = input('输入发件人邮箱:')
    my_password = getpass.getpass('输入发件人邮箱密码(可复制粘贴):')
    recipients = input('输入收件人邮箱:')
    yag = yagmail.SMTP(sender,my_password,'smtp.qq.com')
    yag.send(recipients, '【1901050056】自学训练营学习4群 day11 lyxfree', my_contents)

def stats_text(text,count):#将两个函数做成一个函数
    if type(text)==str:
        all = stats_text_en(text, count) + stats_text_cn(text, count)
        All = ','.join(all)
        return All
    else:
        raise ValueError ('type of argumengt is not str')
