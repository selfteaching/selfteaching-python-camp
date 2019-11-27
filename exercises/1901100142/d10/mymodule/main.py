import stats_word
import traceback
from collections import Counter
from os import path
import json


def load():
    path_this = path.dirname(path.abspath(__file__))
    path_file = path.join(path_this,"tang300.json")
    with open(path_file,'r',encoding = 'utf-8') as f:
        return f.read()
def merge(data):
    poems = ""
    dicts = json.loads(data)
    for item in dicts:
        poems += item.get("contents","")
    return poems
data = load()
text = merge(data)

try:
    dict1_order = stats_word.stats_text_cn(text,100)
    print(dict1_order)
except ValueError as e:
    print("the text needed to be sorted is not a string, please try again!\n",e)