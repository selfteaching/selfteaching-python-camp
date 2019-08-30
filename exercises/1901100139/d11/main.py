
import yagmail
import requests
import pyquery
import getpass
import logging
from mymodule import stats_word


logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

def get_article():
    r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document= pyquery.PyQuery(r.text)
    return document('#js_content').text()

def main():
    try:
        article=get_article()
        result=stats_word.stats_text_cn(article,10)
        logging.info('%s %s',type(result),str(result))
        sender=input('请输入邮箱号：')
        password=getpass.getpass('请输入密码：')
        recipients=input('请输入收件邮箱')
        yag=yagmail.SMTP(sender,password,'smtp.qq.com')
        yag.send(recipients,'【1901100139】⾃学训练营 DAY11 PassionPit',str(result))
        logging.info('已发送')
    except Exception as e:
        logging.exception(e) 
            


if __name__=='__main__':
    main()        