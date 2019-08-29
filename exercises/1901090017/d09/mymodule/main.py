import stats_word
import json
import os #调用os.path 读取文件路径

""" 
open('filename')
在处理文件对象时，最好使用 with 关键字。 优点是当子句体结束后文件会正确关闭
或调用 f.close() 来关闭文件并立即释放它使用的所有系统资源
"""

# 导入json文件并读取文件内容
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'tang300.json')
with open(file_path,'r', encoding='UTF-8') as t: 
# with open('/Users/lihuashan/Documents/GitHub/selfteaching-python-camp/exercises/1901090017/d09/mymodule/tang300.json','r', encoding='UTF-8') as t: #
    print(t)
    read_file = t.read()

# from mymodule import stats_word
''' 1. 捕获传入非字符串参数异常。
    2. 调用stats_word.py中的stats_word_cn(),传入读取文件结果和输出限制参数。
'''
try : 
    print('100中文词频统计结果：', stats_word.stats_text_cn(read_file,10))
except ValueError as ve:
    print(ve)   