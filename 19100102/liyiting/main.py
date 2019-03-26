

"""导入stats_word模块"""
from mymodule import stats_words


with open('tang300.json') as a:
    file1 = a.read()
    a.closed

"""调用stats_words模块中的stats_text函数"""

print("汉字单字出现的结果如下：")
print(stats_word.stats_text_cn(file1,100))