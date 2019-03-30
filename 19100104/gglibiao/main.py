# 这是一个调用stats_word.py模块，统计并输出一段文字中英文和中文词频的程序

'''导入stats_word模块'''
from mymodule import stats_word

with open('tang300.json')as a:
    filel = a.read()
    a.closed
'''调用stats_word模块中的stats_text函数'''

print('汉字单字出现的结果如下：')
print(stats_word.stats_text_cn(filel, 20))