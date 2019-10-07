from mymodule import stats_word
import yagmail
import getpass
import requests
import pyquery
import logging
import lxml
import jieba


logging.basicConfig(format='file:%(filename)s | line:%(lineno)d | message:%(message)s',\
    level=logging.DEBUG)

# 定义提取微信公众号正文的函数
def get_article():
    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    print(r)
    t =r.text
    #print(t)
    d = pyquery.PyQuery(t)
    #print(d)
    article = d('#js_content').text()
    print(article )
    return article




def main():
    try:
        article=get_article()
        result = stats_word.stats_text_cn(article,10)
        # 输出日志信息
        logging.info('%s%s',type(result),str(result))
        #输入邮箱密码
        sender = input('输入发件人邮箱：')
        password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')
        recipients =input('输入收件人邮箱：')
        # 使用163邮箱，host='smtp.163.com'
        # 如果用qq邮箱，host='smtp.qq.com'
        yag = yagmail.SMTP(sender,password,host='smtp.163.com')
        yag.send(recipients, '自学训练营学习14群1901100064-DAY11', str(result))
        #提示信息
        logging.info('已发送，请注意查收')
    except Exception as e:
        #抛出错误
        logging.exception(e)


if __name__ == "__main__":
    main()




