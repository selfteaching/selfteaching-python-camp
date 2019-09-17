from mymodule import stats_word
import getpass
import yagmail
import requests
import logging
from pyquery import PyQuery

# 获取网页内容
def get_content(url):
    # 请求网页返回内容
    response = requests.get(url)
    # 提取微信公众号正⽂
    document = PyQuery(response.text) 
    content = document('#js_content').text()
    return content
# 发邮件
def post_email(content,title):
    sender = input('输⼊发件⼈邮箱:')
    password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):') 
    recipients = input('输⼊收件⼈邮箱:')
    # yag = yagmail.SMTP(sender,password)
    # yag = yagmail.SMTP(sender,password,'smtp.163.com')
    yag = yagmail.SMTP(sender,password,'smtp.qq.com')
    yag.send(recipients,title,content)

def main():
    logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)
    try:
        url='https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
        content = stats_word.stats_text_cn(get_content(url),100)
        # content = '测试！！'
        # print('统计结果：',content)
        # logging.info('%s %s',type(content),str(content))
        post_email(content,'1901100296 自学训练营学习20群DAY11')
        logging.info('已发送，请注意查收！')
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    main()
