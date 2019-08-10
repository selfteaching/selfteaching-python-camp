from mymodule import stats_word
from pyquery import PyQuery
import requests
import getpass
import yagmail

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码(可复制粘贴)：')
recipients = input('输入收件人邮箱：')
#使用requests请求获取返回结果
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
#提取微信公众号正文
document = PyQuery(r.text)
content = document('#js_content').text()
#对提取结果进行词频统计，返回前100词
work_list = stats_word.stats_text_cn(content,100)
#将list返回结果转换为str类型
work_list_new = [str(x) for x in work_list]  #将列表中的int类型转换为str类型
work = ' '.join(work_list_new)  

#通过yagmail登陆自己的邮箱，发送统计结果
subject = '【1901010116】自学训练营学习1群 DAY11 Tiannaxu'
yag = yagmail.SMTP(sender,password,'smtp.163.com')
yag.send(recipients,subject,work)