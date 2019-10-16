from mymodule import stats_word
import logging
import yagmail
import getpass
import pyquery
import requests


logging.basicConfig(format="file:%(filename)s|line:%(lineno)d|message:%(message)s",level=logging.DEBUG)

def test1():
    r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
    document = pyquery.PyQuery(r.text)
    return document("#js_content").text()


def test2():
    try:
        b=test1()
        c=stats_word.stats_text_cn(b,10)
        logging.info('%s %s',type(c),str(c))
        d=input('请输入发件人邮箱：')
        e=getpass.getpass('请输入发件人密码：')
        f=input('请输入收件人邮箱：')
        g=yagmail.SMTP(d,e,host='smtp.qq.com')
        g.send(f,'自学训练营学习2群 李博文',str(c))
        logging.info('已发送')
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    test2()