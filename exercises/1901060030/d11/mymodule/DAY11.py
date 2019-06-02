import requests
from pyquery import PyQuery
from stats_word import stats_text

website ='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
# Import the content from website of "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
response = requests.get(website, auth=('user', 'pass'))

# Extract the content from the source code
document = PyQuery(response.text)
content = document('#js_content').text()

# Leverage function of 'stats_text' to identify the top 100 frequent words 
countlist = stats_text(content,100)
countlist_str = ''.join(str(i) for i in countlist)
print(countlist_str)

# Use getpass to enter the email address related information
import getpass
sender = input('Enter the email address of sender:')
password = getpass.getpass('Enter the password of the email from sender:')
recipients = input('Enter the email address of the reciever:')

# Leverage yagmail to send out email
import yagmail
yag = yagmail.SMTP(user=sender, password=password, host='smtp.gmail.com')
yag.send(recipients, '自学训练营学习5群DAY11 wwwo0916', countlist_str)
