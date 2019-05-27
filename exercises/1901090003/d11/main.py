from mymodule import stats_word

# file = open('/Users/Justco/selfteaching-python-camp/exercises/1901090003/d09/tang300.json','rb')
# text1 = file.read()
# text = text1.decode()

# print(stats_word.stats_text_cn(text,20))

# file.close()

import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
print(response)

from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()
print(stats_word.stats_text_cn(content,100))
# 输入你的账号密码，注意密码是授权码
# 然后你打开你的qq邮箱
# 发送成功了，刚才你没有设置服务器smtp.qq.com
# 现在好了，可以关闭了

import yagmail
user = input('账号')
password = input('mi ma')
smp = 'smtp.qq.com'
yagmail.SMTP(user=user,password=password,host=smp).send('pythoncamp@163.com', '【1901090003】自学训练营 DAY11 minidv963', str(stats_word.stats_text_cn(content,100)))

