from mymodule import stats_word  

#通过网络请求获得网页内容，使用分词工具对中文字符串进行分词，统计词频，得出结果，发送给到指定的邮箱

import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery
document=PyQuery(response.text)
content=document('#js_content').text()
email_content = str(stats_word.stats_text_cn(content))
print (email_content)

import getpass
sender=input('请输入发件人邮箱：')
password=getpass.getpass('输入发件人邮箱密码(可复制粘贴):')    # 无回显 密码防止泄露
# print (password)                                            # 当然也可以自己测试下打印下 是否真的 输入了内容,用完之后 一定记得删除
recipient=input('请输入收件人邮箱：')


import yagmail
yag=yagmail.SMTP(sender,password,"smtp.qq.com")
yag.send(recipient,'1901100277 自学训练营学习19群 Day11 xuefeng365',email_content)
