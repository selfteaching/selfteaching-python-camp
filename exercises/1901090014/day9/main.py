from models.stats_word_09 import *
a=123131
b='sas'

with open('E:/练习/selfteaching-python-camp/exercises/1901090014/day9/tang300.json', 'r', encoding='utf-8') as file:
    str = file.read()
count=100
try:
    print(f'输出词频最高的前100个汉字词频：{stats_text_cn(str,count)}')
except :
    print('are you sure this is a string')
