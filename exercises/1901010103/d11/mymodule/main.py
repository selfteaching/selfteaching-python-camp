#!/usr/bin/python
import yagmail
import requests
import getpass
import sys
from pyquery import PyQuery
sys.path.append('/Users/Yang/GitHub:PJ1/selfteaching-python-camp/exercises/1901010120/d11/mymodule/')
from stats_word import stats_text
from os import path

#提取微信地址和正文
content_url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
html_code = requests.get(content_url).text
document = PyQuery(html_code)
content = document("#js_content").text().replace("\n", "")


#file_path = path.join(path.dirname(path.abspath(__file__)),'./tang300.json')
#with open(file_path,'r', encoding="utf-8") as f_poems:
#    poems_json = json.load(f_poems)

#all_poems = ""
#for poems_info in poems_json:
#    all_poems += poems_info["contents"]

try:
    en_result, cn_result = stats_text("",content)
    #print cn_result
    smtp_host = "smtp.sina.com"
    sender = input("Please enter the sender's email address: ")
    password = getpass.getpass("Please enter the sender's email password: ")
    recipient = input("Please enter the recipient's email address: ")
    yagmail.SMTP(user=sender, password=password, host=smtp_host).send(recipient, "Cutted words", str(cn_result))
except ValueError as e:
    print("Exception catched.")
    print(e)