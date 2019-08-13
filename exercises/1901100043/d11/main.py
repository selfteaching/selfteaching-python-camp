from mymodule import stats_word
from pyquery import PyQuery
import yagmail
import getpass
import logging
import requests

logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

def main():
    try:
        r =requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
        document = PyQuery(r.text)
        article  = document('#js_content').text() # 提取内容
        result   = stats_word.stats_text_cn(article,100)
        logging.info('%s %s',type(result), str(result))

        sender = input('请输入发件人邮箱：')
        password = getpass.getpass('请输入发件人邮箱密码：')
        recipients = input('请输入收件人邮箱：')

        yag = yagmail.SMTP(sender,password,'smtp.qq.com')
        yag.send(recipients,'自学训练营13群 1901100043 潘勇',str(result))
        
        logging.info('已发送，请注意查收。')
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    main()

'''
实战1：
step 1: r = requests.get(url) 获得网页内容
step 2: pyquery 解析网页内容。



'''