import mymodule.stats_word as stats_word
import requests
from pyquery import PyQuery
import yagmail
import getpass



sort_list = {}
try:
    sender = input('输⼊入发件⼈人邮箱:')
    password = getpass.getpass('输⼊入发件⼈人邮箱密码(可复制粘贴):') 
    recipients = input('输⼊入收件⼈人邮箱:')
 
    url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
    response = requests.get(url,verify = False)
    document = PyQuery(response.text) 
    content = document('#js_content').text()
    #对列表中中英文字符，进行统计降序排列
    sort_list = stats_word.stats_text(content,100)

    yag = yagmail.SMTP(user = sender, password = password, host='smtp.qq.com')

    # 邮箱正文
    contents = str(sort_list)

    # 发送邮件
    yag.send(recipients, '【自学训练营学习9群】⾃自学训练营 DAY11 keqi-jj',contents)

except ValueError as result:
    print(result)
except:
    print('用户名、密码或者接受者用户名异常！')


