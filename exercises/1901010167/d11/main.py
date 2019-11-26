from mymodule import stats_word
import yagmail
import requests
from pyquery import PyQuery
import getpass
if __name__ == "__main__":
    try:
        r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
        docs = PyQuery(r.text)
        content = docs('#js_content').text()
        result=stats_word.stats_text(content,100,0)
        result=str(result)
        print(result)
        sender=input("输入发件人邮箱：")
        password = getpass.getpass("输入发件人邮箱密码（可复制粘贴）：")
        recipients=input('输入收件人邮箱:')
        yag = yagmail.SMTP(user = sender, password = password, host = 'smtp.qq.com')
        yag.send(to = recipients, subject = '[1601010167]+自学训练营学习2群+GordonPQB', contents =result)
    except ValueError :
        print('输入的为非字符串')

                          