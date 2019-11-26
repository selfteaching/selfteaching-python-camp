

from stats_word import stats_text_cn
import yagmail
import requests
import getpass

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') 

from pyquery import PyQuery
document = PyQuery(response.text) 
content = document('#js_content').text()

sender = input("输入发件人邮箱:")
password = getpass.getpass("输⼊发件人邮箱密码(可复制粘贴):") 
recipients = input("输入收件人邮箱:")


result = stats_text_cn(content,100)
result1 = str(result)
print(result1)

yag = yagmail.SMTP(sender,password,host='smtp.qq.com')
contents = ["文章《张小龙4小时“拖堂”演讲，全面总结微信8年（官方完整版）》使用频率最高的100个词：",result1]
yag.send('pythoncamp@163.com', '自学训练营学习3群 DAY11 moxiyun', contents)
print("发送成功！")