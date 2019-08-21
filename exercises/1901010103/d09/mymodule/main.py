#!/usr/bin/python
import sys
sys.path.append('/Users/Yang/GitHub:PJ1/selfteaching-python-camp/exercises/1901010120/d08/mymodule/')

from stats_word import stats_text
from os import path
import json

file_path = path.join(path.dirname(path.abspath(__file__)),'./tang300.json')
with open(file_path,'r', encoding="utf-8") as f_poems:
    poems_json = json.load(f_poems)

all_poems = ""
for poems_info in poems_json:
    all_poems += poems_info["contents"]

try:
    en_result, cn_result = stats_text("", all_poems)
    print("EN words result: ", en_result)
    print("CN words result: ", cn_result)
except ValueError as e:
    print("Exception catched.")
    print(e)