import stats_word
import yagmail
import requests
import getpass
from pyquery import PyQuery

def main():
    response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(response.text)
    words = document('#js_content').text()
    #结果
    result = str(stats_word.stats_text_cn(words))
    #登录邮箱并发送结果
    sender = input('发件邮箱')
    password = getpass.getpass('密码')
    recipients = input('收件人')
    title = input('标题')
    yag = yagmail.SMTP(sender,password,'smtp.126.com')
    yag.send(to=recipients,subject=title,contents=result)

if __name__ == '__main__':
    main()