from mymodule import stats_word
from pyquery import PyQuery
import yagmail
import getpass
import requests
import json
from wxpy import *
count = 100
import requests

bot = Bot()
my_friends = bot.friends()

@bot.register(my_friends,SHARING)
def my_friends_sharing(msg):
    response = requests.get(msg.url)
    document = PyQuery(response.text)
    contents = document('#js_content').text()
    result = str(stats_word.stats_text_cn(contents,20))
    msg.reply(result)

embed()

#sender = input('请输入发件人邮箱：')
#password = input('请输入发件人邮箱密码：')
#recipents = input('请输入收件人邮箱：')
#yag = yagmail.SMTP(user=sender,password=password,host='smtp.gmail.com')
#yag.send(to= recipents, subject= '自学营008期01班 day11 SelenaX113', contents= '统计结果为：' + '\n' + result)
# try:
#     stats_word.stats_text_cn(text,count)
# except ValueError:
#     print('Invalid string')
