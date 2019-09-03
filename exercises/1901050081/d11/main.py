import getpass
from pyquery import PyQuery as pq
import requests
from mymodule import stats_word
import yagmail

sender = input('输入发件人邮箱：')
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）：')

url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
response = requests.get(url)
html = response.text

doct = pq(response.text)
doct_text = doct('#js_content').text()

result = stats_word.stats_text_cn(doct_text)
result_words = str(result)
print(isinstance(result_words,str))

yagmail.register(sender,password)
yag=yagmail.SMTP(sender,password,'smtp.qq.com')
yag.send('pythoncamp@163.com','自学训练营学习7群 QueenieQ2019',result_words)
print('发送成功！')