
import stats_word
import json
count = 20
with open('C:\\Users\\jinzh\\Documents\\GitHub\\selfteaching-python-camp\\19100204\\jinzhijian77\\mymodule\\tang300.json',encoding='UTF-8') as a:
    text = a.read()

'''调用stats_word模块中的stats_text函数'''

print(stats_word.stats_text_cn(text,count))

