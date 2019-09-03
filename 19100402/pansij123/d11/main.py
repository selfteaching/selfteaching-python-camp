from modules.stats_word import stats_text_cn as st
import json
from pyquery import PyQuery as pq
import yagmail
import requests as rq
import getpass

print("Getting web content...")
#comments are below the command
r=rq.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
# r, request web page
q=pq(r.text)
# q, pyquery the r
t=q('#js_content').text()
# t, content of the q
#OK print(type(t))
#OK #print(t)

#-stat words- in t#
print("Statting cn words...")
try:
	s = st(t,101)
	#print(s[1:100])
	print(type(s))
	string = ''
	for i in s:
		string+=(str(i))
	print(string)
	print(type(string))

except TypeError:
	print("\nFrom main.py:\tInput should be string if you see an error above")

print("\nThe above information of word stats will be sent to the following email: ")
emailto='pythoncamp@163.com'
print(emailto)
emailfrom=input('Please input your email. We will use this email to hand in your assginment.\n')
emailpass=getpass.getpass('Please input your password. It will not echo.\n')
contents=['19100402 pansij123\nBelow is an str: \n',string,'\nThanks.']
#yag.send('pythoncamp2019@gmail.com', 'hello', contents)
print('OK.\nSending email...')
yagmail.SMTP(emailfrom,emailpass).send(emailto,'19100402 day11 @pansij123',contents)
print('Completed.')
