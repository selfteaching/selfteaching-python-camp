# day 11
import yagmail
import getpass
import requests
from mymodule import stats_word as sw

sender = input('Please input sender mailaddress:')
password = getpass.getpass('Please input sender mailcode:')
recipients = input('Please input recipients addresses:')
smtp = 'smtp.126.com'

# 提取微信公众号正文
from pyquery import PyQuery
response = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
document = PyQuery(response.text)
content = document('#js_content').text()
statString = str(sw.stats_text(content,100))

#WHY THERE UNDERLINED? 'https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA'

#copied from @wengyadong, need to explore further, what's sw?...

#my_stats = str(sw.stats_text(content, 100))
#print(my_stats)


yagmail.SMTP(sender,password,smtp).send(recipients,'19100302 catynchyna', statString)


#copied from @wangrui0802
# def stats(url,num):
#     response = requests.get(url)
#     document = PyQuery(response.text)
#     content = document('#js_content').text()


#     statList = sw.stats_text(content,num)
    
#     statDict = dict(statList)
#     return statDict

# day_11 = stats('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',100)
# print(day_11)