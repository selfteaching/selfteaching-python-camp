import requests
from pyquery import PyQuery
import re
import jieba
from collections import Counter
import getpass
import yagmail

'''获取目标目标网页内容，类型是一个HTTP'''
response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
'''提取http文件中p之间的内容'''
document = PyQuery(response.text)
content = document('p').text()


'''用正则去掉文本中的数字，字母和符号'''
content = re.sub('[a-zA-Z0-9’!"%&\'^\s+|\s+$()*+,-./:;，。?、…？“”‘’！]+',"",content)
'''用jieba将文本进行全模式切分'''
seg_list = jieba.cut(content, cut_all=True)
'''用counter统计词频'''
result = Counter()
for seg in seg_list:
        if len(seg) > 1:
            result[seg] = result[seg] + 1
mydic = result.most_common(100)
'''返回一个对象的string格式'''
mystr = str(mydic)

'''连接服务器，用yagmail发送邮件，此处的password为邮箱的授权码，非邮箱登录密码'''
sendSmpt = yagmail.SMTP(user = input('请输入发件人邮箱:'),
password=getpass.getpass('请输入发件人邮箱密码(可复制粘贴):'),host='smtp.163.com')
sendSmpt.send(to = input('请输入收件人邮箱:'),subject="19100104 imjingjingli",contents=mystr)
