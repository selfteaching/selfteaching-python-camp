
#调用所需库及函数
import yagmail
import requests
import getpass
from pyquery import PyQuery
import stats_word


#获取网页内容
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_coment').text()
print(content)#测试
#处理内容
result = stats_word.stats_text_cn(content)
result_str = ''.join(str(i) for i in result)
print(result_str)

#登陆邮件并发送结果
sender = input('请输入发件人邮箱:')
psw = getpass.getpass('输入发件人邮箱密码（可复制粘贴):')
recipients = input('输入收件人邮箱：')
smtp = 'smtp.qq.com'

yagmail.SMTP(sender,psw,smtp).send(recipients,'自学训练营学习3群DAY11 xiaoqie007',result_str)
