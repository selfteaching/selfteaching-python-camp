import requests    # 请求获得内容
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

from pyquery import PyQuery    # 解析提出内容
document = PyQuery(response.text)
content = document('#js_content').text()

import mymodule.stats_word    # 导入模块运行公式
result = str(mymodule.stats_word.stats_text(content))    # 结果转换str类型

import getpass
sender = input('发件人邮箱：')
password = getpass.getpass('发件人邮箱密码:')
#recipients = input('收件人邮箱:')

import yagmail
yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com')
#yag.send(to= recipients, subject= '19100105 quan0523', contents= result)
yag.send(to= ['pythoncamp@163.com','116986035@qq.com'], subject= '19100105 quan0523',contents= result)