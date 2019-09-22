text = '''
The zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#任务1：使用字典（dict）统计字符串串样本 text 中各个英文单词出现的次数
text1 = text.replace(","," ").replace("."," ").replace("-", " ").replace("*", " ").replace("!"," ")
#先把text中的符号剔除掉
text2 = text1.lower()   #把所有的单词变成小写或者大写
text2 = text2.split()  #把text变成list格式
d = {}   #采用字典形式保存结果
for i in text2:    
    a = text2.count(i)
    d[i] = a  #统计text2中i的频次，并将结果导入字典
d1 = sorted(d.items(), key = lambda item : item[1], reverse = True) #将结果按照字典中的value排序
print(d1)






