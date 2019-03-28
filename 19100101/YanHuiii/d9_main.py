#这是一个调用stats_word.py模块，统计并输出一段文字中英文和中文词频的程序
  

"""导入stats_word模块"""
from mymodule import d9_stats_word
import json


with open('tang300.json') as a:
    file1 = a.read()
"""调用stats_word模块中的stats_text函数"""

print("汉字单字出现的结果如下：")
print(d9_stats_word.stats_text_cn_count(file1,100))


