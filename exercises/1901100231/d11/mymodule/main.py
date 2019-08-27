import json#加载json模块完成对.json文件的读取
import stats_word
import jieba
import requests
import yagmail
from pyquery import PyQuery
import getpass
sender = input('输⼊发件⼈邮箱:')
password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):')
recipients = input('输⼊收件⼈邮箱:')#获取用户的邮箱和密码
#获取词频统计结果
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()#微信公众号文章的内容被提取到了content变量中
output = stats_word.stats_text_cn(content,100)
output = str(output)#将结果转换为str类型
#发送邮件
yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com')
try:
    yag.send(recipients,'自学训练营学习18群 Day11 CHJ219',output)
    print('邮件发送成功')
except :
    print('邮件发送失败，请检查原因。')