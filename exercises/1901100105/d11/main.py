import yagmail
import requests
import pyquery
import getpass
import logging
from mymodule import stats_word

# 在anacoda prompt中用pip --version命令查看version.命令pip install requests/PyQuery, pip3 install yagmail[all]
# 在国内时安装pip用清华镜像 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests yagmail pyquery lxml

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s', level=logging.DEBUG)

#提取微信公众号文章正文
def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article, 100)
        logging.info('%s%s', type(result), str(result))
        sender = input('请输入发件人邮箱：')
        #以下是为保护密码，输入密码时不会显示出来，直接输入后回车
        password = getpass.getpass('输入发件人邮箱密码：')
        recipients = input('请输入收件人邮箱：')
        #以下对应邮箱，修改gmail
        yag = yagmail.SMTP(sender, password, 'smtp.gmail.com') #测试成功，回复不符合规定已被拦截
        yag.send(recipients, '[1901100105]自学训练营学习16群DAY11 Nanananashi', str(result))
        logging.info('已发送，请注意查收。')
    except Exception as e:
        logging.exception(e)

           
if __name__ == '__main__':
    main()
    



