import requests
import pyquery
import yagmail
import getpass
from mymodule import stats_word
from pyquery import PyQuery

#提取微信公众号正文
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()

#将获得的文章进行分词
text = stats_word.stats_text_cn(content,100)
text1 = str(text)

#登录邮箱并发送结果
fajian=input('输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码：')
shoujian=input('输入收件人邮箱：')

yag=yagmail.SMTP(fajian,password,'smtp.163.com')
yag.send(shoujian,'19100402 zhangshuzhong',text1)
