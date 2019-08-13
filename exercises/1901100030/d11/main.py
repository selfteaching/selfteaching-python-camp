# day11 实战应用
# 2019年7月22日
# 陈浩 学号 1901100030

import logging
import yagmail
import requests
import pyquery
import getpass
from mymodule import stats_word

# 初始化logging模块
logging.basicConfig(format="file:%(filename)s|line:%(lineno)d|message:%(message)s",level=logging.DEBUG)

# 定义获取文章函数
def get_article():
    r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
    document = pyquery.PyQuery(r.text)
    return document("#js_content").text()

def main():
    try:
        article = get_article()
        result = stats_word.stats_text_cn(article, 10)
        logging.info("%s %s", type(result), str(result))
        sender = input("请输入发件人邮箱：")
        password = getpass.getpass("请输入邮箱密码：")
        recipient = input("请输入收件人邮箱：")
        yag = yagmail.SMTP(sender, password,"SMTP.126.com")
        yag.send(recipient, "自学训练营13群 1901100030", str(result))
        logging.info("已发送，请注意查收。")
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()



