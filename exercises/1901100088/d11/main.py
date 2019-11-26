from mymodule import stats_word
import os
import requests
from pyquery import PyQuery
import getpass
import yagmail

def get_data():
    """从获取微信文章数据
    """
    response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
    document = PyQuery(response.text)
    content = document('#js_content').text()
    outcome = str(stats_word.stats_text_cn(content,100))
    return(outcome)

def send_mail():
    """通过yagmail发送邮件
    """
    sender = input('输⼊发件人邮箱:')
    mima = getpass.getpass('输⼊发件人邮箱密码(可复制粘贴):')
    recipients = input('输⼊收件人邮箱:')
    yag = yagmail.SMTP(user = sender, password = mima, host="smtp.qq.com")
    yag.send(recipients, '【1901100088】自学训练营15群 DAY11 Meroy92', get_data())


if __name__ == "__main__":
    try:
        send_mail()
    except TypeError:
        print("Oops!  That was no string.  Try again...")
    except AttributeError:
        print('Sorry, there is a AttributeError')