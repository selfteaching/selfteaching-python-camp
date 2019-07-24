#-*- coding:utf-8 -*-
#import mymodule.stats_word
import io
import sys
import jieba
import requests
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from pyquery import PyQuery
import yagmail
import getpass

#统计中文字频的函数
def stats_text_cn(t):   
 
     word_str=''
     word_lst = []
     word_lst1 = []
     word_dict = {}
     exclude_str = "，。！？、（）【】<>《》=：+-*—“”…"
     cnt=Counter()
     count=100
      # 添加每一个字到 新字符串中
     for i in t: 
        if u'\u4e00' <= i <= u'\u9fff':
            word_str=word_str+i

     #print(word_str) 
     word_list=jieba.lcut(word_str, cut_all=False)     
     #print(word_list) 
     for i in word_list:
         if len(i) >= 2:
            word_dict[i] = word_list.count(i)

     cnt = Counter(word_dict)
     r=cnt.most_common(count)
     print(r)
     print(type(r))
     return r


url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"; # 需要请求的网址
response = requests.get(url)  # 发送Get请求
#print(response.text)  # 得到结果并输出Text属性的值，得到网页的内容
# 提取微信公众号正文
document = PyQuery(response.text)
content = document('#js_content').text()
#print(content)

result= str(stats_text_cn(content))



#通过yagmail登录自己的邮箱，将统计结果发送到pythoncamp@163.com 
#标题：19100105 baishanheishui
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码(可复制粘贴):')
                 
mail = yagmail.SMTP(user=sender,password=password,host='smtp.163.com')
mail.send(to=['pythoncamp@163.com','15309888203@163.com'], subject='19100105 baishanheishui',contents=result) 