# 安装依赖包 requests yagmail pyquery lxml
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests yagmail pyquery lxml

import yagmail
import requests
import pyquery
import getpass
import logging
from mymodule import stats_word

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message: %(message)s', level=logging.DEBUG)
# 提取微信公众号文章正文
def get_particle():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()

def main():
    try:
        article = get_particle()
        result = stats_word.stats_text_cn(article, 10)
        logging.info('%s %s', type(result),str(result))
        sender = input('请输入发件人邮箱：')
        # 为了保护密码，输入密码的时候不会显示出了，直接出入，完成后按回车就行
        password = getpass.getpass('请输入发件人邮箱密码')
        recipients = input('请输入收件人邮箱：')
        # 如果使用的是QQ邮箱这里就填smtp.qq.com
        yag = yagmail.SMTP(sender, password, 'smtp.163.com')
        yag.send(recipients, '自学营009期01班,Github名：liangqs2019,学号：1901100020,Day11 work', str(result))
        logging.info("已发送，请注意查收。")
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()


    