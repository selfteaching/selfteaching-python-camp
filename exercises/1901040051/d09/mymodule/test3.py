# from collections import Counter
# #首先导入Counter类
# lst=['this','is','a','test','just','a','test','you','shoud','believe','in','this','me','just','a','test','a','test','a','test']
# #构建一个列表
# word_count=Counter(lst)
# #首先对列表的元素进行一次统计
# top_three=word_count.most_common(3)
# #调用most_common方法找出最多的元素
# print(top_three)
# #输出结果[('test', 5), ('a', 5), ('just', 2)]

from collections import Counter
#首先导入Counter类
lst=['this','is','a','test','just','a','test','you','shoud','believe','in','this','me','just','a','test','a','test','a','test']
#构建一个列表
word_count=Counter(lst)
#首先对列表的元素进行一次统计
top_three=word_count.most_common(3)
#调用most_common方法找出最多的元素
print(top_three)
#输出结果[('test', 5), ('a', 5), ('just', 2)]

