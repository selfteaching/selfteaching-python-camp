import requests # 网络请求库
from pyquery import PyQuery # 文档解析库
from stats_word import stats_text_cn    # 统计中文词频
import yagmail  # 邮件模块
import getpass

response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
#print(response.text)

# 提取微信公众号正文伪代码
document = PyQuery(response.text) 
content = document('#js_content').text()

# 设置邮箱信息
sender=input('输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码(可复制粘贴)：')
recipients=input('输入收件人邮箱：')
smtp='smtp.exmail.qq.com'
yag=yagmail.SMTP(sender,password=password,host=smtp)

# 统计前100个中文词频
count=100
try:
    result=str(stats_text_cn(content,count))
    print(f'输出词频前100的词和词频数：{result}')
except ValueError as e:
    print('ValueError:',e)

# 将结果发送邮件
yag.send(to=recipients,subject='自学训练营学习7群 Day11 hpy729',contents=result)

print('Mission Complete!')