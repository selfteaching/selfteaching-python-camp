#使用requests请求微信公众号文章
import requests
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

#用pyquery提取正文
from pyquery import PyQuery
document = PyQuery(r.text)
content = document('#js_content').text()

#用stats_word对提取结果进行分析和前100词（100词的筛选在函数那个文件里已经设置了），结果转换成str
from mymodule  import stats_word 
result = str(stats_word.stats_text_cn(content))

#通过yagmail登录邮箱，发送统计结果
import yagmail
import getpass
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）:')
recipients = input('输入收件人邮箱:')
smtp = 'smtp.qq.com'
yag = yagmail.SMTP(user=sender,password=password,host=smtp)
yag.send(to=recipients,subject='自学训练营学习7群DAY11 josedweck',contents=result)
print('发送成功')

    
