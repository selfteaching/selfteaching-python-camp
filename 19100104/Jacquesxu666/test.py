#coding=utf-8
from mymodule import stats_word as sw
from pyquery import PyQuery
import requests
import yagmail
import getpass


r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

document = PyQuery(r.text)
content = document('#js_content').text()
sw.stats_text(content, 100)
