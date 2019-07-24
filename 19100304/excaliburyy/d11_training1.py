# 19100304 day11 银零
# 1.使用 request 请求 参考资料4 微信公众号文章的链接，获取返回结果(response)
# 2.将response.text 用 pyquery 把微信公众号正文提取出来
# 3.使用 stats_text 对提取结果进行分析和词频统计处理（返回前100个词的统计结果），将结果转换成str类型
# 4.通过 yagmail 登录自己的邮箱，将统计结果发送到 pythoncamp@163.com （标题格式：班级编号+GitHub用户名）





import yagmail
import requests
import pyquery
from pyquery import PyQuery
from mymodule import stats_word

url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
response = requests.get(url)
document = pyquery.PyQuery(response.text)
content = document('#js_content').text()
list_content = stats_word.stats_text_cn(content,100)
string_content = ''.join(list_content)

import getpass

sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')

yag = yagmail.SMTP(user=sender,password=password,host='smtp.qq.com')
yag.send(recipients,'19100304 excaliburyy',string_content)

