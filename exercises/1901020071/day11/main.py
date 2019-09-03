from mymodule import stats_word
from collections import Counter

import jieba
import requests
from pyquery import PyQuery
import yagmail
import getpass

response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")

document=PyQuery(response.text)
content = document('#js_content').text()



#把文件里的汉字进行词频统计，并返回
countList=stats_word.stats_text_cn(content,100)
countList=str(countList)



mygmailusername=input("请输入你的邮箱转发地址")
mygmailpassword=getpass.getpass("请输出你的邮件密码")
receivemail = input("请输入你的邮箱接收地址")
yag = yagmail.SMTP(mygmailusername, mygmailpassword,"smtp.sina.com")
yag.send(receivemail, '自学训练营学习1群 DAY11 shuaidu108',countList)

#seg_list=jieba.cut(text,cut_all=False)
#print("default mode:",", ".join(seg_list))

