# this is d6 excercise for modules
# date : 2019.3.24
# author by : qiming
# modified by : Luchen
# 延用上次作业，完善本次内容。

from mymodule import stats_word


with open('tang300.json') as f:#文件读取失败，暂未得到解决
    read_file = f.read()
try : 
    print('汉字字频最高的前100字统计结果： ', stats_word.stats_text_cn(f,100))
except ValueError as ve :
    print(ve)

