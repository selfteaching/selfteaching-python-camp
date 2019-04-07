import requests
from pyquery import PyQuery
import re
import jieba
from collections import Counter
import getpass
import yagmail

#获取网页内容
response=requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
content = document('p').text()


#用正则去掉文本中的数字，字母和符号
content = re.sub('[a-zA-Z0-9’!"%&\'^\s+|\s+$()*+,-./:;，。?、…？“”‘’！]+',"",content)

#用jieba将文本进行处理
seg_list = jieba.cut(content, cut_all=True)
result = Counter()
for seg in seg_list:
        if len(seg) > 1:
            result[seg] = result[seg] + 1
mydic = result.most_common(100)

#返回一个对象的string格式
mystr = str(mydic)


sendSmpt = yagmail.SMTP(user = input('请输入发件人邮箱:'),
password=getpass.getpass('请输入发件人邮箱密码(可复制粘贴):'),host='smtp.qq.com')  
sendSmpt.send(to = input('请输入收件人邮箱:'),subject="19100104 gglibiao",contents=mystr)