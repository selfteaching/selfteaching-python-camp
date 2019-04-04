import requests
from mymodule import stats_word
import json
import os
import sys
from pyquery import PyQuery
import yagmail
import getpass
#能加载的全都加上

r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
response = r.text

#document = PyQuery(response.text)
#对不起，我之后再研究PyQuery

#print('字频最高的前100字统计结果： ', stats_word.stats_text_cn(response))
result_list = stats_word.stats_text_cn(response)
#print(type(result_list))

#result_str = "".join(result_list)
'''for i in result_list:
    print result_list[i].__str__())
''' #tup没有成功转换成str

sender = input('发件邮箱：')
password = getpass.getpass('邮箱密码')
recipients = input('收件邮箱')

yag = yagmail.SMTP()
contents = [result_list]
yag.send('pythoncamp@163.com', '19100303 Luchen1471', result_list)

