import stats_word
import yagmail
import requests
import getpass
from pyquery import PyQuery

def main():
    #获取网页内容
    response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    document = PyQuery(response.text)
    content = document('#js_content').text()
    #处理文本
    result = stats_word.stats_text_cn(content,count=100)
    #登录邮箱并发送结果
    sender = input('输入发件人邮箱:')
    password = getpass.getpass('输入发件人邮箱密码:')
    recipients = input('输入收件人邮箱:')
    title = input('输入标题:')
    yag = yagmail.SMTP(sender,password,'smtp.qq.com')
    yag.send(to=recipients,subject=title,contents=str(result))
    
if __name__=='__main__':
    main()