import requests
from pyquery import PyQuery
import stats_word
import getpass
import yagmail

response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text) 
content = document('#js_content').text()
stats = stats_word.stats_text_cn(content,100)
string=str('')
for unit in stats:
    if len(unit[0]) <= 2:
        string += "'" + unit[0] + "'的频率是:    " + str(unit[1]) + "\n"
    elif len(unit[0]) == 3:
        string += "'" + unit[0] + "'的频率是:  " + str(unit[1]) + "\n"

sender = 'yanning931231@sina.com'
password = '7c50817e1ffff142'
recipients = '604332298@qq.com'
print(type(sender))
yag = yagmail.SMTP(sender,password)
print(type(password))
yag.send(to=recipients,subject='[你好]',contents=string)
print('done')