import re
import sys
import jieba
import getpass
import yagmail
from mymodule import stats_word
#import json
#with open('tang300.json','r',encoding='UTF-8') as f:
   # text=f.read()

#print(stats_word.stats_text_cn(text,20))
import requests
from pyquery import PyQuery
from mymodule import stats_word


response = requests.get("https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA")
document = PyQuery(response.text)
content = document('#js_content').text()
return stats_word.stats_text_cn(content,100)
print(stats_word.stats_text(content,100))

