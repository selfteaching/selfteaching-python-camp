from mymodule import stats_word
import requests
from pyquery import PyQuery
import getpass
import yagmail

if __name__ == '__main__':
    sender = input('输⼊发件⼈邮箱:')
    password = getpass.getpass('输⼊发件⼈邮箱密码(可复制粘贴):')
    recipients = input('输⼊收件人邮箱:')

    r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

    document = PyQuery(r.text)
    content = document('#js_content').text()
    
    print('统计中文词频:')
    result = stats_word.stats_text_cn(content, 100)
    print(result)

    yag = yagmail.SMTP(sender, password, host="smtp.163.com")
    yag.send(recipients, '【1901100019】自学训练营学习12群 DAY11 shaoguos', result.__str__())