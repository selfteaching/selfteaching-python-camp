from mymodule import stats_word
import re
import logging
import requests
from pyquery import PyQuery
import yagmail
import getpass

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制黏贴）：')
recipients = input('输入收件人邮箱：')
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

document = PyQuery(response.text)
content = document('#js_content').text()
logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)d|%(message)s',level=logging.DEBUG)

def main():
    try:
        logging.info('result===>%s',stats_word.stats_text_cn(content,100))
        contents = str(stats_word.stats_text_cn(content,100))
        yag = yagmail.SMTP(sender,password,host='smtp.163.com')
        yag.send(recipients,'【1901090061】自学训练营11群DAY11 王辉',contents)
    except Exception as e:
        logging.exception(e)


if __name__== '__main__':
    main()
