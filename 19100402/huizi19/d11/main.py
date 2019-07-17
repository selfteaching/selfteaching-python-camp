from mymodule import stats_word 
import  requests
from pyquery import PyQuery
import  yagmail
import  getpass

response= requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码：')
recipients = input('输入收件人邮箱：')


yag = yagmail.SMTP(user=sender,password=password,host='smtp.163.com')
contents = str(dict(stats_word.stats_text_cn(content,100)))
yag.send(recipients,'19100402 huizi19',contents)