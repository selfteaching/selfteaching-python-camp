import requests
from pyquery import PyQuery
from mymodule import stats_word
import yagmail
import getpass

r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
response_text = r.text

document = PyQuery(response_text)
content = document('#js_content').text()

result = stats_word.stats_text_cn(content)


sender = input('请输入发件人邮箱：')
password = input('请输入发件人邮箱密码：')
recipents = input('请输入收件人邮箱：')
yag = yagmail.SMTP(user=sender,password=password,host='smtp.163.com')
yag.send(to= recipents, subject= '自学营008期01班 day11 TonyGai', contents= '统计结果为：' + '\n' + result)