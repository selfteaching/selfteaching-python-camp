import requests
from pyquery import PyQuery as pq
import getpass
import stats_word
import yagmail


#get the information of the web
url = 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'
r = requests.get(url)
#get all the content of the web
document = pq(r.text)
content = document('#js_content').text()
#get the useful text by the pyquery way
#print(content)

try:
    dict1_order = stats_word.stats_text_cn(content,100)
    #get the order of the 100th number
    print(str(dict1_order))
    sender = input('输入发件人邮箱')
    password = getpass.getpass('输入发件人邮箱密码：')
    recipients = input('输入收件人邮箱：')

    yag = yagmail.SMTP(sender,password,'smtp.163.com')
    yag.send(recipients,'自学训练营16群suyaoyong',str(dict1_order))
except ValueError as e:
    print("the text needed to be sorted is not a string, please try again!\n ",e)
    #this sentence is use to print the information of the exception


