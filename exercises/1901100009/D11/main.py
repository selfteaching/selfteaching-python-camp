import yagmail
import requests
import pyquery
import getpass
import logging
from mymodule import stats_word


# 安装包 request yagmail pyquery lxml
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple request yagmail pyquery lxml

logging.basicConfig(format = 'file=%(filename)s|line:%(lineno)d|message:%(message)s',level = logging.DEBUG)

def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article,20)
        logging.info('%s %s' ,type(result),str(result))
        '''
        sender = input('请输入发件人邮箱：')
        password = getpass.getpass('请输入密码：')
        recipients = input('请输入收件人邮箱：')
        yag = yagmail.SMTP(sender,password,'smtp.126.com')
        yag.send(recipients,'自学训练营学习12群 1901100009',str(result))
        logging.info("已发送，请注意查收")
        '''
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    #stats_word.stats_text(1)
    main()