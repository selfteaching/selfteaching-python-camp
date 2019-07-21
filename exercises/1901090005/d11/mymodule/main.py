
import stats_word
import requests
import yagmail
import pyquery
import getpass
count = 100

reponse = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery
document = PyQuery(reponse.text)
content = document('#js_content').text()
string = str(stats_word.stats_text_cn(content,count))
# print(string)

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输⼊收件人邮箱:')
yag = yagmail.SMTP(sender,password,'smtp.qq.com') 
yag.send(recipients,'自学营008期01班ElleZhou_Day11',string)



