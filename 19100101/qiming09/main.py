# this is d10 excercise for 3rd-party library
# date : 2019.3.27
# author by : qiming

with open('tang300.json') as t :
    ''' 1. 导入json文件并读取文件内容'''
    read_file = t.read()
t.closed

from mymodule import stats_word
''' 1. 捕获传入非字符串参数异常。
    2. 调用stats_word.py中的stats_text_cn(),传入读取文件结果和输出限制参数。
'''
try : 
    print('Top20中文词频统计结果： ', stats_word.stats_text_cn(read_file,20))
except ValueError as ve :
    print(ve)
