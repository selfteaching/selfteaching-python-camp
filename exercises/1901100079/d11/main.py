from mymodule import stats_word
import logging
import yagmail
import pyquery
import requests
import getpass
import socket

hostname = socket.gethostname()
print(hostname)

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG) 
# %(filename)s: 打印当前执行程序名；%(lineno)d: 打印日志的当前行号；%(message)s: 打印日志信息；level: 设置日志级别，debug是打印全部的日志,详细的信息,通常只出现在诊断问题上。

def get_artical():
    art=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') 
    doc=pyquery.PyQuery(art.text)
    return doc('#js_content').text()

def main():
    try:
        a=get_artical()
        output=stats_word.stats_text_cn(a,100)
        logging.info('%s %s',type(output),str(output))
        sender = input('输⼊发件⼈邮箱:')
        password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):')
        recipients = input('输⼊收件⼈邮箱:')
        yag=yagmail.SMTP(sender,password,'smtp.163.com')
        yag.send(recipients,'【1901100079】⾃学训练营学习15群 DAY11 Zmoon73',str(output))
        logging.info('已发送，请注意查收！')
    except Exception as i:
        logging.exception(i)
    
if __name__=='__main__':
    main()         