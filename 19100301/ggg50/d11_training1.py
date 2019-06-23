
import requests
import getpass
import yagmail

from pyquery import PyQuery
from mymodule import stats_word_day10



response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
r_content = document('#js_content').text()


sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')


yag = yagmail.SMTP(sender,password, host='smtp.qq.com')
