import stats_word
import traceback
from collections import Counter
from os import path


# -*- coding: uft-8 -*-


#text = stats_word.text
def load():
    path_this = path.dirname(path.abspath(__file__))
    path_file = path.join(path_this,"tang300.json")
    with open(path_file,'r',encoding = 'utf-8') as f:
        return f.read()
text = load()
try:
    dict1 = stats_word.stats_text(text)
    dict_order = Counter(dict1).most_common(19) 
except ValueError as e:
    print("the text needed to be sorted is not a string, please try again!\n ",e)
    #this sentence is use to print the information of the exception
    #print(traceback.format_exc())
print(dict_order)