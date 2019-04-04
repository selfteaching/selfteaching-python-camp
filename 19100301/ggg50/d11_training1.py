import requests
import getpass
import yagmail
from os import path
from pyquery import PyQuery
from mymodule import stats_word_day10



path_file = path.join(path.dirname(path.realpath(__file__)), "tang300.json")

response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
r_content = document('#js_content').text()

# input text and define output word numbers
send_content = stats_word_day10.stats_text_cn(r_content, 100)
print(str(stats_word_day10.stats_text_cn(r_content, 100)))

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:') 


yag = yagmail.SMTP(sender,password, host='smtp.qq.com')
yag.send(to="pythoncamp@163.com",subject = "19100101 ggg50", contents = str(send_content))


