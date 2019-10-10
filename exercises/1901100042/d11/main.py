import getpass
import yagmail
import stats_word
import logging
import requests
import pyquery

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

#提取微信公众号文章正文
def get_article():
    words = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(words.text)
    return document('#js_content').text()

def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article,10)
        logging.info("%s %s",type(result),str(result))

        #下面为发邮件内容
        sender =input('请输入您的邮箱地址：')
        password = getpass.getpass('请输入您的密码（可复制）：')
        recipients = input ('请输入收件人邮箱地址：')
        yag = yagmail.SMTP(sender,password,'smtp.qq.com')
        yag.send(recipients,'自学训练营学习13群  1901100042',str(result))
        logging.info("邮件已发送，请查收！")
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main()
