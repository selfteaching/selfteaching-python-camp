# this is d6 excercise for modules
# date : 2019.3.24
# author by : qiming
# modified by : Luchen
# 延用上次作业，完善本次内容。+1

from mymodule import stats_word
import json
import os
import sys

#with open('tang300.json') as f:#文件读取失败，暂未得到解决
    #read_file = f.read()
#try : 
    #print('汉字字频最高的前20字统计结果： ', stats_word.stats_text_cn(f)) #20这个参数内置在函数里了
#except ValueError as ve :
    #print(ve)

#f = open('tang300.json')还是不成功

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json')) as f: #还是不成功
    read_file = f.read()
    #print(f) 
    #print(f.read)
    #print(read_file)
    #print('汉字字频最高的前20字统计结果： ', stats_word.stats_text_cn(f))
    print('汉字字频最高的前20字统计结果： ', stats_word.stats_text_cn(read_file))

#ValueError: type of argumengt is not str  好像我在stast_text_cn里加载的f或者f.read，并不是一个str才导致的错误。