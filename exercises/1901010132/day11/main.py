import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats_word
import getpass
import yagmail
# 抓取网页
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# 提取正文
document = PyQuery(r.text)
content = document('#js_content').text()
print(content)

#词频统计并转为str类型
#wordString = ''.join(str(i) for i in wordList)
word_list = stats_word.stats_text_cn(content,100)
word_str = str(word_list) #转换成str类型
print(word_str)

#发送统计结果到指定邮箱
sender = input('请输入发件人邮箱:')
psw = getpass.getpass() #授权码
recipients = input('输入收件人邮箱：') #指定邮箱pythoncamp@163.com
smtp = "smtp.qq.com" #服务器地址

yagmail.SMTP(sender,psw,smtp).send(recipients,'【1901010132】自学训练营学习2群DAY11 bamboo',word_str)