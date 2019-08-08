import requests
import yagmail
import pyquery
import getpass
import logging
from mymodule import stats_word

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)
  
# https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA
def get_article():
    r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')  #request 请求提取网页正文
    document = pyquery.PyQuery(r.text)     # pyquery 提取正文
    return document('#js_content').text()    # 提取微信公众号正文伪代码

def main():  # try-except  捕获可能的异常 和  logging+exception 捕获异常
    try: 
        artical=get_article()
        result=stats_word.stats_text_cn(artical,100)    # 调用了 stats_word.py的编程 获取前十高频词  此处变量是article,
                            #而 article从get_article得到，get_article又从上个def得到。？？def的项目如何找到对应项目？？
        logging.info('%s %s',type(result),str(result))  #此处 loggine.info 相当于print
        sender=input('请输入发件人邮箱：')
        password=getpass.getpass('请输入发件人邮箱密码：')
        recipients=input('请输入收件人邮箱：')
        yag=yagmail.SMTP(sender,password,'smtp.163.com')
        yag.send(recipients,'自学训练营学习16群 Day11 1901100123',str(result))
        logging.info('已发送，请注意查收。')
        #logging.info(data[0])  #显示 打印出字符串的第一个符号， 不懂哦 
    
    except Exception as e:
        logging.exception(e)



if __name__ == "__main__":
    main()
