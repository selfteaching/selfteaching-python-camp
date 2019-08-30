import stats_word
import json
import jieba

# 导入json文件并读取文件内容
with open('/Users/lihuashan/Documents/GitHub/selfteaching-python-camp/exercises/1901090017/d10/mymodule/tang300.json','r', encoding='UTF-8') as t: #
    read_file = t.read()

# from mymodule import stats_word
''' 1. 捕获传入非字符串参数异常。
    2. 调用stats_word.py中的stats_word_cn(),传入读取文件结果和输出限制参数。
'''
try : 
    print('100中文词频统计结果：', stats_word.stats_text_cn(read_file,20))
except ValueError as ve:
    print(ve)   