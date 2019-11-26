import requests
from pyquery import PyQuery
from os import path
import json

def load_file():
    #获取文件路径的方式，要确保 tang300.json 跟当前文件在同一文件夹下，这两种方式等价
    file_path = path.join(path.dirname(path.abspath(__file__)), './tang300.json')

    # 采用 with 语句打开文件，并将打开文件作为结果返回
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        return text


# 7. 通过 module 功能 将统计词频的 stats_word.py 导入到此文件中，并完成本文件中汉字及英文字符，并输出

from stats_word import stats_text, stats_text_en, stats_text_cn

test_text = load_file()

# 5. 通过 requests.get 获得 微信公众号文章，存入 response 
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# 6. 提取 response 对应的公众号 正文

document = PyQuery(response.text) 
content = document('#js_content').text()

try:
    # 调用 stats_text 函数 并将输出结果保存到 dict 类型数据 dict_EnCn 中
    stats_text_cn(content, 5)
except ValueError:
    print("请用字符串作为文件内容")

count = 100

# 调用 stats_text_cn 函数，将所有汉字及出现的频次记录在 字典 dict_EnCn 中
dict_EnCn = dict(stats_text_cn(content, count))

#按照出现次数从大到小并输出前count 指定数目的汉字和英文单词及出现次数
#内置函数 sorted 的参数 key 表示按元素的那一项的值进行排序
# dict 类型 counter 的 items 方法会返回一个 包含 相应 项 （key, value）的 元组 列表
print('从大到小输出所有的单词及汉字出现的次数==>', sorted(dict_EnCn.items(), key=lambda x: x[1], reverse=True))

dict_str = str(dict_EnCn)

print(dict_str)

import yagmail
username = '63270646@qq.com'#邮箱账号
passwd = 'ugqfgvmtvccybhfh'#授权码，不是邮箱密码
yag = yagmail.SMTP(user=username, password=passwd, host='smtp.qq.com', smtp_ssl=True)

import getpass
sender = input('输入发件⼈邮箱:')
password = getpass.getpass('输入发件⼈邮箱密码(可复制粘贴):')
recipients = input('输入收件人邮箱:')
#TODO: 在下面实现分词统计和发送邮件的操作
yag.send(
    to=['63270646@qq.com'], #如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
    cc=['63270646@qq.com','pythoncamp@163.com'], #抄送
    subject='自学训练营学习10群 Charles-qian-jh',#邮件标题
    contents='你好，今天终于成功了'+ dict_str,#邮件正文
    attachments=[r'C:\Users\钱晓辉\result.txt'])#附件如果只有一个的话，用字符串就行