# 从mymodule文件夹中调用stats_word.py
from mymodule import stats_word
from pyquery import PyQuery
import requests
import getpass
import yagmail

if __name__ == "__main__":
    # 获取requests对象
    rsp = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    # 提取微信公众号正文伪代码
    document = PyQuery(rsp.text)
    text = document('#js_content').text()
    try:
        content = stats_word.stats_text_cn(text)
        user = input('Please enter the sender\'s email address:')
        password = getpass.getpass('Please enter the sender\'s email password:')
        recipient = input('Please enter the recipient\'s email address:')
        yag = yagmail.SMTP(user,password,'smtp.qq.com',smtp_ssl=True)
        yag.send(recipient,'【1901040001】自学训练营3群 DAY11 XiaCongcong',content)
    except ValueError:
        print('The input is a non-string, please enter a string.')