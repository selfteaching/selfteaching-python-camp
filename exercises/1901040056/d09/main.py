import mymodule
with open('tang300.json') as t:
    ''' 1. 导入json文件并读取文件内容'''
    read_file = t.read()

from mymodule import stats_word
''' 1. 捕获传入非字符串参数异常。
    2. 调用stats_word.py中的stats_text_cn(),传入读取文件结果和输出限制参数。
'''
try : 
    print('100中文词频统计结果：', stats_word.stats_text_cn(read_file,100))
except ValueError as ve:
    print(ve)   