from mymodule import stats_word

# file = open('/Users/Justco/selfteaching-python-camp/exercises/1901090003/d09/tang300.json','rb')
# text1 = file.read()
# text = text1.decode()

# print(stats_word.stats_text_cn(text,20))

# file.close()

#使⽤requests请求微信公众号⽂文章的链接

import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
print(response)


#将response.text⽤用pyquery把微信公众号正⽂文提取出来
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()

#使⽤用stats_word中的stats_text对提取结果进⾏行行分析和词频统计处理理(返回前100个词的 统计结果)
print(stats_word.stats_text_cn(content,100))

#通过yagmail登录⾃自⼰己的邮箱，将统计结果发送邮件
import yagmail
user = input('账号:')
password = input('密码:')
smp = 'smtp.qq.com'
yagmail.SMTP(user=user,password=password,host=smp).send('pythoncamp@163.com', '【1901090003】自学训练营 DAY11 minidv963', str(stats_word.stats_text_cn(content,100)))



