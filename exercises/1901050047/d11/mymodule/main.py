import requests  # 网络请求库
from pyquery import PyQuery  # 文档解析库
from stats_word import stats_text_cn  # 统计中文词频
import yagmail  # 发送邮件
import getpass  # 交互式密码模块

response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')    # 发送请求,url对应的页面内容
#print(response.text)    # 获取返回的HTML信息,字符串str

document = PyQuery(response.text)     # 传入HTML代码

content = document('#js_content').text()

count = 100  # 统计100个中文词汇

try:      
    r_list = stats_text_cn(content,count)   # 统计前100个中文词频
    r_str = str(r_list)  # 转换成str类型
    print(r_str)
   
except Exception as e:  # 检查中文词频异常
    print('ValueError =>', e) 

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码(可复制粘贴):')
host = "smtp.sina.com"  # SMTP服务器地址
yag = yagmail.SMTP(sender,password,host)

recipients = input('输入收件人邮箱:')  
subject = '自学训练营学习4群 DAY11 klpk011'
yag.send(recipients, subject, r_str)   # 收件人，主题，正文

print('发送完成')
