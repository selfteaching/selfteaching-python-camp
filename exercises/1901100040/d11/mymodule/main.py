import requests
import stats_word
from pyquery import PyQuery
import getpass
import yagmail

r = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
#从指定网站中请求信息

document=PyQuery(r.text)
content = document('#js_content').text()
#提取微信公众号正⽂

sender = input("输入发件人邮箱：")
password = getpass.getpass("输入发件人邮箱密码:")
recipients = input("输入收件人邮箱:")

a=stats_word.stats_text_cn(content,100)
b=str(a)
print(b)
#调用stats_word.py文件中的stats_text_cn函数实现：把提取到的文本分词降序排序

yag=yagmail.SMTP()
yag.send(recipients,'pythoncamp@163.com', '自学营009期01班 DAY11 Four-Leaf-Clover', b) 



