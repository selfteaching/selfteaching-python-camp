import stats_word
from collections import Counter
import jieba
import requests
from pyquery import PyQuery
import yagmail
import getpass
import logging

# 使⽤requests 请求参考资料4微信公众号⽂章的链接，获取返回结果(response)
# 获得一个名为 response 的 Response 对象。我们可以从这个对象中获取所有我们想要的信息。
# response 的类型class 'requests.models.Response'？？
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

# 使用PyQuery
document = PyQuery(response.text) 
content = document('#js_content').text() # <class 'str'>
print(content)

try : 
    result = stats_word.stats_text_cn(content,100)
    print('100中文词频统计结果：', result)
    logging.info('%s %s', type(result), str(result))
    sender = input('请输入发件人邮箱：')
    password = getpass.getpass('请输入发件人邮箱密码：')
    recipients = input('请输入收件人邮箱：')
    yag = yagmail.SMTP(sender, password, host='smtp.qq.com')
    yag.send(recipients, '自学训练营学习8群 day11 1901090017', str(result))
    logging.info("已发送，请注意查收。")
    

except Exception as e:
    logging.exception(e)

 
 