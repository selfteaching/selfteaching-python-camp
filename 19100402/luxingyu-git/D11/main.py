from mymodule import stats_word
from pyquery import PyQuery
import requests
import getpass
import yagmail 
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入（或者复制）发件人邮箱密码（授权码）:')
recipients = input('输入收件人邮箱:')

url = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(url.text)        
content = document('#js_content').text()   

str1 = str(dict(stats_word.stats_text_cn(content,100)))
yag = yagmail.SMTP(sender,password,'smtp.qq.com') 
yag.send(recipients,'19100402 luxingyu-git',str1)