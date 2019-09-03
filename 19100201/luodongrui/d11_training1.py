import yagmail
import requests
import getpass

sender = input('输入发件人邮箱:' '843435679@qq.com')
password = getpass.getpass('输入发件人邮箱密码：' '35582580.')
recipients = input('输入收件人邮箱:' 'pythoncamp@163.com')
smtp = 'smtp.qq.com'

from pyquery import PyQuery

response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
content = document('#js_content').text()

import stats_word

contents = stats_word.stats_text_cn(content)
conents= ''.join(str(i) for i in contents)
counter=100
print("""---提取前100个词的统计结果---""")


yagmail.SMTP(sender,password,smtp).send(recipients,'19100201 luodongrui',contents)


