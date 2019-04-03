from pyquery import PyQuery
import yagmail

import getpass

r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',auth=('user','pass'))
document=pyquery.PyQuery(r.text)
content=document('#js_content').text()

mdict=[]
strResult=''
try:
    mdict=stats_word.stats_text_cn(text)
except:
    print("error:",sys.exc_info()[0])

strResult=','.join([str(x) for x in mdict])


# document = PyQuery(response.text)
# content = document('#js_content').text()


sender = input('输入发件人邮箱')
password = getpass.getpass('输入发件人邮箱密码:')
recipients = input('输入收件人邮箱:')

yag = yagmail.SMTP('zzfuture1983', 'password')
yag.send('recipients', 'test yagmail', 'This is the body')

# sender = input('Please input your email address:')
# password = getpass.getpass('Please input your password:')
# recipients = input('Please input the recipients:')
# title = input('Please input the title:')
# yag = yagmail.SMTP(sender,password)
# yag.send(recipients,'19100303 张正', 'oh just testing.')