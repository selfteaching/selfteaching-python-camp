from mymodule import stats_word            #它是输入stats_word

import json  
path=r'D:\selfteaching-python-camp\exercises\1901010056\d09\tang300.json'
with open(path,'r',encoding='UTF-8') as f: #不加'r', encoding='UTF-8'会报UnicodeDecodeError
                                                      #然后是打开，tang300.josn
    read_date = f.read()                              #把这个josn读出来，然后在关闭


try:

    print('统计字数最多的前100个字： \n',stats_word.stats_text_cn(read_date,100)) ##然后就是打印出执行后的文本

except ValueError as w:   

    print(w)  