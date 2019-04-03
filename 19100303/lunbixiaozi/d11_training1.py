from pyquery import PyQuery
import yagmail
import requests
import getpass
import mymodule.stats_word

Inscription = '''
Best regards
Zheng Zhang
MBA, Class of 2019, Stephen M. Ross School of Business
Tauber Institute for Global Operations
University of Michigan

'''

r=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',auth=('user','pass'))
document=PyQuery(r.text)
content=document('#js_content').text()

counter_cn_dict = mymodule.stats_word.stats_text_cn(content, 100)
counter_cn_string = str(counter_cn_dict)

mail_body = 'Hi \nHere are the most common 100 words in the speech: \n' + counter_cn_string + '\n\n' + Inscription
print (mail_body)

sender = input('输入发件人邮箱: ')
password = getpass.getpass('输入发件人邮箱密码: ')
recipients = input('输入收件人邮箱: ')

yag = yagmail.SMTP('zhz@umich.edu', password)
yag.send(recipients, '19100303 lunbixiaozi', mail_body)
