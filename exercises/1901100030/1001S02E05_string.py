#<<<<<<< master
# day5 字符串练习
# 2019年7月9日
#=======
# day4 流程控制练习
# 2019年7月9日
# 内容：数据容器学习
#>>>>>>> master
# 陈浩 学号 1901100030


text = '''
The Zen of Python, by Tim Peters
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
# 1替换单词
text = text.replace("better","worse")
print (text)

# 2剔除单词
words = text.split()
#print(words)
#定义一个临时变量，存放过滤后的单词
filered = []
for word in words :
    if word.find("ea") < 0 :
        filered.append(word)
print(filered)

# 3大小写翻转
#<<<<<<< master
#swapcased = []
#for word in filered:
#    swapcased.append(word.swapcase())
swapcased = [i.swapcase() for i in filered]
#=======
swapcased = []
for word in filered:
    swapcased.append(word.swapcase())
#>>>>>>> master
print(swapcased)

# 4升序排列
print(sorted(swapcased))