from mymodule import stats_word10            #它是输入stats_word
import re
import json  
import jieba
path=r'D:\selfteaching-python-camp\selfteaching-python-camp\exercises\1901010056\d10\tang30010.json'
with open(path,'r',encoding='UTF-8') as f: #不加'r', encoding='UTF-8'会报UnicodeDecodeError
                                                      #然后是打开，tang300.josn
    read_date = f.read()                              #把这个josn读出来，然后在关闭


stats_word10.stats_text_cn(read_date,20) ##然后就是打印出执行后的文本

