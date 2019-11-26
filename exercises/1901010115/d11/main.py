from mymodule import stats_word #读取模块
import json #引入jsan解码库
import jieba

import getpass #引入提示代码？此处不太懂。如果要发送邮件，需从哪里输入邮箱信息
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients = input('输入收件人邮箱：')

import requests #引入requests库
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') #用get语法直接获取网页HTML代码

from pyquery import PyQuery as pq #引入pyquery库
doc = pq(r.text) #用pq()语法解析网页的HTML代码
content = doc('#js_content').text() #引入提示代码？此处完全不懂该语法原理。得到文字文本
result = stats_word.cn(content,100) #用stats——word模块的函数处理文本，筛选出词频最高的100个词
result_str = str(result) #将结果转为字符串

import yagmail #插入yagmail库
yag = yagmail.SMTP(sender,password,host='smtp.qq.com') #链接邮箱服务器。此处不懂为何有问题？
yag.send(recipients,'[1901010115]自学训练营DAY11 游业鹏',result_str) #设定接收人、标题、内容信息后，发送