import stats_word
import traceback
from collections import Counter
from os import path
import json


#text = stats_word.text
def load():
    #load the tang300.json file
    path_this = path.dirname(path.abspath(__file__))
    path_file = path.join(path_this,"tang300.json")
    with open(path_file,'r',encoding = 'utf-8') as f:
        return f.read()
def merge(data):
    #get the poems from the file, use the get method of dictionary
    poems = ""
    dicts = json.loads(data)
    for item in dicts:
        poems += item.get("contents","")
    return poems
data = load()
text = merge(data)

try:
    dict1_order = stats_word.stats_text_cn(text,100)
    #get the order of the 100th number
    print(dict1_order)
except ValueError as e:
    print("the text needed to be sorted is not a string, please try again!\n ",e)
    #this sentence is use to print the information of the exception
    #print(traceback.format_exc())
