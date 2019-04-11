#!/usr/bin/python3
# Filename: main.py
import ssl
import stats_word

import json
import jieba

with open(r'''C:\Users\ZGY\Documents\GitHub\selfteaching-python-camp\19100402\zhengguanya\d09\mymodule\tang300.json''','r+',encoding="utf-8") as f:
    string1 = f.read()

try:
    stats = stats_word.stats_text_cn(string1)
except ValueError:
    print("ValueError: You have an input that is not a string.")
else:
    print(stats)


import requests
r = requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA',verify=False)
from pyquery import PyQuery
document = PyQuery(r.text)
content = document('#js_content').text()
print(content)