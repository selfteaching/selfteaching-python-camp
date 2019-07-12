#获取微信公众号文章进行词频统计后，用邮箱发送结果

#引用
from pyquery import PyQuery
import requests
from mymodule import stats_word
import getpass
import yagmail

#获取微信公众号文章
wechat = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(wechat.text)
content = document('#js_content').text()
#print(content)

#对文章进行词频分析
wx = stats_word.stats_text(content)
wechat_word = ''.join(str(i) for i in wx)

#wechat_word.encode('utf-8').decode('utf-8')
print(wechat_word)

#用yagmail登录自己邮箱发出邮件

#设置邮箱发送
sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')

#引用yagmail发送文件
yag = yagmail.SMTP(sender,password,'smtp.163.com')
yag.send(recipients,'19100205 ss412231878',wechat_word)
