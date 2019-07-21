from pyquery import PyQuery
import requests
import mymodule.stats_word
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text) 
content = document('#js_content').text()
result = mymodule.stats_word.stats_text_cn(content, 100)
print(result)
convert_result_to_str = ''.join(str(i) for i in result)
print(convert_result_to_str)

import yagmail
import getpass
yag = yagmail.SMTP('appgler@qq.com')
contents = ['下面是qianwanliang统计的结果：...']
yag.send('pythoncamp@163.com', '19100205 qianwanliang', contents)
sender = input('输入发件人邮箱:') 
password = getpass.getpass('输入发件人邮箱密码（可复制粘贴）:')
recipients = input('输入收件人邮箱:')