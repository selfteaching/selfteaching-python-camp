import requests
import stats_word
import pyquery
import getpass
import yagmail
import logging

logging.basicConfig(format='file:%(filename)s[line:%(lineno)d]message:%(message)s',level=logging.DEBUG)

#提取公众号正文
def get_article():
    r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
    document = pyquery.PyQuery(r.text)
    return document('#js_content').text()


def main():
    try:
        article = str(get_article)
        result=stats_word.stats_text_cn(article,100)
        #调用stats_word.py文件中的stats_text_cn函数实现：把提取到的文本分词降序排序
        logging.info('%s %s',type(result),str(result))
        sender = input("输入发件人邮箱：")
        password = getpass.getpass("输入发件人邮箱密码:")
        recipients = input("输入收件人邮箱:")
        yag=yagmail.SMTP(sender,password,'stmp.qq.com')
        yag.send(recipients,'pythoncamp@163.com', '自学营009期01班 DAY11 Four-Leaf-Clover', str(result)) 
        logging.info("已发送，请注意查收。")
    except Exception as e:
        logging.exception(e)
        
if __name__=="__main__": 
    main()