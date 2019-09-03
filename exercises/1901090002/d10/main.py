from mymodule.stats_word import *

with open('documents/selfteaching-python-camp/exercises/1901090002/d10/tang300.json','r',encoding='utf-8') as file:
    str = file.read()

print(stats_text_cn(str,20))