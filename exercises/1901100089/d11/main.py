from mymodule import stats_word
import logging
import yagmail
import requests
import pyquery
import getpass

# 安装依赖包 requests yagmail pyquery lxml
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests yagmail pyquery lxml

logging.basicConfig(format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)


# 提取微信公众号文章正文
def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article,10)
        logging.info('%s %s',type(result),str(result))
        sender = input('请输入发件人邮箱：')
        # 为了保护密码，输入密码的时候不会显示出来，直接输入，完成后按回车执行
        password = getpass.getpass('输入发件人邮箱密码：')
        recipients = input('请输入收件人邮箱：')
        # 如果使用的是QQ邮箱，这里就填 smtp.qq.com
        yag = yagmail.SMTP(sender,password,'smtp.qq.com')
        yag.send(recipients,"自学训练营学习15群 1901100089",str(result))
        logging.info("已发送，请注意查收。")
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    main()


