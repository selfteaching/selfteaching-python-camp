from mymodule import stats_word

file = open('/Users/Justco/selfteaching-python-camp/exercises/1901090003/d09/tang300.json','rb')
text1 = file.read()
text = text1.decode()

print(stats_word.stats_text_cn(text,20))

file.close()

import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
print(response)

from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()
print(stats_word.stats_text_cn(content,100))

import yagmail
yagmail.SMTP('3636655@qq.com').send('pythoncamp@163.com', '【1901090003】自学训练营 DAY11 minidv963', 'stats_word.stats_text_cn(content,100)')

