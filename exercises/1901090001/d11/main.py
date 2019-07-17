from mymodule import stats_word
from pyquery import PyQuery
import yagmail
import getpass
import requests
import json
count = 100

import requests
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
response_text = r.text
document = PyQuery(response_text)
contents = document('#js_content').text()

result = str(stats_word.stats_text_cn(contents,100))

sender = input('请输入发件人邮箱：')
password = input('请输入发件人邮箱密码：')
recipents = input('请输入收件人邮箱：')
yag = yagmail.SMTP(user=sender,password=password,host='smtp.163.com')
yag.send(to= recipents, subject= '自学营008期01班 day11 SelenaX113', contents= '统计结果为：' + '\n' + result)
# try:
#     stats_word.stats_text_cn(text,count)
# except ValueError:
#     print('Invalid string')
