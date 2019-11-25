import stats_word
import yagmail
import getpass
import requests
from pyquery import PyQuery as pq

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = pq(response.text)
content = document('#js_content').text()
result = stats_word.stats_text_cn(content,100)
result_str = str(result)
username = input('输⼊入发件⼈人邮箱:')
passwd = getpass.getpass('输⼊入发件⼈人邮箱密码(可复制粘贴):')
recipients = input('输⼊入收件⼈人邮箱:')
subject = '【1901100368】自学训练营学习21群 DAY11 skyli007'
mail = yagmail.SMTP(user=username, password=passwd, host='smtp.163.com', smtp_ssl=True)#smtp_ssl=True 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话
mail.send(to= recipients,subject = subject, contents = result_str)
print('发送成功')