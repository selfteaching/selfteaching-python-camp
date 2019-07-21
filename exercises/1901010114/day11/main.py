from mymodule import stats_word
import os
import json
count = 100



import os
import json
import requests
import pyquery

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA', auth=('user', 'pass'))
response.status_code
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()


content1=(stats_word.stats_text_cn(content,100))
for i in content1:  #将输出结果转化成str形式，google搜索来
    print(i, end="")

import getpass
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码(可复制粘贴):')
recipients = input('输入收件人邮箱:')


 
 



