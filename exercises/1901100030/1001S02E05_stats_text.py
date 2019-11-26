# day5 字符串练习
# 2019年7月9日
# 陈浩 学号 1901100030

text = '''
The Zen of Python, by Tim Peters
#<<<<<<< master

#=======
#>>>>>>> master
Beautiful is better than ugly. 
Explicit is better than implicit.
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
elements = text.split()
#<<<<<<< master
print(elements)
#=======

#>>>>>>> master
# 定义新存储变量
words = []
# 定义待剔除的符号
symbols = ",.*-!"
# 遍历所有元素，剔除特殊符号
for element in elements:
    for symbol in symbols:
        element = element.replace(symbol,"")
    if len(element):
        words.append(element)
print(words)

# 初始化字典
counter = {}
# 定义集合，剔除重复元素，降低遍历次数
words_set = set(words)
#print(words_set)
#根据单词进行遍历、统计
for word in words_set:
    counter[word] = words.count(word)
print(counter)

# 2按照出现次数，进行排序，并输出
print(sorted(counter.items(), key=lambda x:x[1], reverse=True ))
