# Import the 微信文章 from the webside
import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# Transer the 微信文章 to string type
from pyquery import PyQuery
document = PyQuery(response.text) 
content = document('#js_content').text()

# Make the satistic of the frequency of the word and output as a string
import stats_word
stats = stats_word.stats_text_cn(content,100)
string=str('')      # Create a string to store the result
for unit in stats:
    # Control the spacing by adding two more space it the word is less than two
    if len(unit[0]) <= 2:
        string += "'" + unit[0] + "'的频率是:    " + str(unit[1]) + "\n"
    elif len(unit[0]) == 3:
        string += "'" + unit[0] + "'的频率是:  " + str(unit[1]) + "\n"

# Send the result to the email
import yagmail
import getpass
sender = input('输⼊入发件⼈人邮箱:')
password = getpass.getpass('输⼊入发件⼈人邮箱密码(可复制粘贴):')       # The password typed will be invisible but will still work
recipients = input('输⼊入收件⼈人邮箱:')
yag=yagmail.SMTP(sender,password,host='smtp.sina.com')
yag.send(to=recipients,subject='自学训练营学习19群+Ningziyun',contents=string)