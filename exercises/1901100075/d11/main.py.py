from mymodule import stats_word
import yagmail
import requests
import pyquery
import getpass
import logging


logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

# 提取微信公众号正⽂
def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')# 使⽤ requests 请求 参考资料4 微信公众号⽂章的链接，获取返回结果（response）
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()



def main():
    try:        
        article=get_article()
        result=stats_word.stats_text_cn(article,100)
        logging.info('%s %s',type(result),str(result))
        sender = input('输⼊发件⼈邮箱:')
        password = input('输⼊发件⼈邮箱密码:')
        recipients = input('输⼊收件⼈邮箱:')
        yag = yagmail.SMTP(sender, password , 'smtp.qq.com')
        yag.send(recipients,'自学训练营14群DAY11 linknight423',str(result))
        logging.info("已发送，请注意查收。")
    except Exception as e:
        logging.exception(e)



if __name__ == '__main__':
    main()



        
    




