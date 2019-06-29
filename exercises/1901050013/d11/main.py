import yagmail
import requests
import getpass
from pyquery import PyQuery
from mymodule.stats_word import stats_text_cn

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') # acquire the article link.
document = PyQuery(response.text)
content = document('#js_content').text() #acquire the article content.
result = str(stats_text_cn(content)) #convert the list type into string type.

sender = input('plese input your email address:')
password = getpass.getpass('please input your password:')
recipients = input('plese input the recipients:')
subject = input('please input the subject:')
yag = yagmail.SMTP(sender,password,'smtp.qq.com')
yag.send(to=recipients,subject=subject,contents=result)