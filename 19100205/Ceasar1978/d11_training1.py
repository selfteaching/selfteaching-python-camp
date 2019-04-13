import requests
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA') 
# 以上通过requests请求文章链接，获取网页内容


from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text() # 将网页内容提取为一个字符串文本作为输入

# print(content)


import mymodule.stats_word


try:
    if not isinstance(content,str):
        raise ValueError()
    
except ValueError:
    print('输入的不是文本格式，请重新输入：')   
dic = mymodule.stats_word.stats_text_cn(content) # 调用函数进行分词并统计词频
str_1 = str(dic) # 将词频统计结果（字典形式）转换成字符串
print(str_1)


import getpass
sender = input('请输入发件人邮箱:')
password = getpass.getpass('请输入发件人密码:')
recipients = input('请输入收件人邮箱:') # 调用getpass避免显示自己的邮箱和密码

import yagmail
yag=yagmail.SMTP( sender, password, host='smtp.qq.com')
yag.send(recipients,'19100205 Ceaar1978', str_1) # 调用yagmail库发送邮件
#请输入发件人邮箱:4655438@qq.com
#Warning: Password input may be echoed.
#请输入发件人密码:cerirwzrinsgcaie
#请输入收件人邮箱:pythoncamp@163.com

