import re
import json
import sys
import collections
from collections import Counter
sys.path.append("c:")
import stats_word

  



with open("mymodule/tang300.json", "r", encoding="utf-8") as file:
    read_data = file.read() 
    read_data = re.sub('[^\u4e00-\u9fff]+', " ", read_data)
file.closed

template1 = 1


mdict={}

try:
    mdict=stats_word.stats_text(template1)
except:
    print("error:",sys.exc_info()[0])
    raise

    
print(mdict) #原顺序以字典形式输出
print(sorted(mdict.items(), key=lambda d: d[1],reverse=True)) #排序后以列表形式输出
''' 1. 捕获传入非字符串参数异常。
    2. 调用stats_word.py中的stats_text_cn(),传入读取文件结果和输出限制参数。
'''
try : 
    print('Top20中文词频统计结果： ', stats_word.stats_text_cn(read_file,20))
except ValueError as ve :
    print(ve)





#     read_data = file.read() 
#     # print(read_data)

# try:

#     result = stats_word.stats_text_cn(read_data)
#     # print(type(result))
#     # # from collections import Counter
#     # # #首先导入Counter类
#     # # lst=['this','is','a','test','just','a','test','you','shoud','believe','in','this','me','just','a','test','a','test','a','test']
#     # # #构建一个列表
#     word_count=Counter(read_data)
#     #首先对列表的元素进行一次统计
#     top_three=word_count.most_common(10)
#     #调用most_common方法找出最多的元素
#     print(top_three)
#     #输出结果[('test', 5), ('a', 5), ('just', 2)]



# except ValueError as e:

#     print(e)