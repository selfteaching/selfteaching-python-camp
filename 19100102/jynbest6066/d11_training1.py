'''调用collections的Counter函数'''
import collections
import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats_word 
import yagmail
import getpass

url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
'''使用requests的get获取网址全部内容'''
response = requests.get(url)

'''使用pyquery提取网址正文内容'''
document = pyquery.PyQuery(response.text)
content = document('#js_content').text()

'''调用stat_word的main程序返回分词结果'''
words = stats_word.main(content)
#print(words)

def count(list3, count):
    return collections.Counter(list3).most_common(count)

top100 = ','.join([str(x) for x in count(words, 100)])



print(top100)
#print(collections.Counter(words).most_common(100))

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
recipients = input('输入收件人邮箱：')

yag = yagmail.SMTP(sender, password, 'smtp.qq.com')

subject = '19100102 jynbest6066'

yag.send(to = recipients, subject = subject, contents = top100)