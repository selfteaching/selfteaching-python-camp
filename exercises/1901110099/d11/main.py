
# 使用 requests 请求 参考资料料4 微信公众号文章的链接，获取返回结果（response）
import requests
response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# 提取微信公众号正⽂
from pyquery import PyQuery
document = PyQuery(response.text)
content = document('#js_content').text()

# 使用 stats_word 中的 stats_text 对提取结果进行分析和词频统计处理（返回前100个词的统计结果），将结果转换成 str 类型
from mymodule import stats_word
result = str (stats_word.stats_text(content,100))
#print (result)

# 用下面的方式实现邮箱和密码的输入
import getpass
sender = input('输入发件人邮箱:')
password = getpass.getpass('输入发件人邮箱密码(可复制粘贴):')
#print(password)
recipients = input('输入收件人邮箱:')

# 发送邮件
import yagmail
yag = yagmail.SMTP(sender,password,'smtp.163.com')
yag.send(to= recipients, subject='1901110099 自学训练营20群 Day11 oli9', contents= result)
