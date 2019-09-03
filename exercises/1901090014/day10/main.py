from models.stats_word_10 import *

with open('E:/练习/selfteaching-python-camp/exercises/1901090014/day10/tang300.json', 'r', encoding='utf-8') as file:
    str = file.read()
    count=20
    try:
        print(f'输出词频最高的前20个汉字词频：{stats_text_cn(str,count)}')
    except :
        print('are you sure this is a string')
