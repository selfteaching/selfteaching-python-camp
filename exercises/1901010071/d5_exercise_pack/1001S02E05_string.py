t = '''
The Zen of Python, by Tim Peters
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

# 作业要求：
# 1.将'better'全部替换成'worse'输出
# 2.从上一步的结果里将包含‘ea’的单次删除
# 3.从第2步的结果中将单词的大小写翻转
# 4.从第3不的结果中将所有单词按'a~z'降序排列

t = t.replace('better','worse') #.replace(olde,new[,count]),count如果定1的话那么就只有第一处会被替换，不给的话全替换
print(t)

t = t.swapcase() # 逐个替换大小写,这一步必须上前，不然的话会报错
print(t)

t = t.replace(',',' ').replace('.',' ').replace('!',' ').replace('*',' ').replace('--',' ') # 去除标点符号
t = t.split() # 拆分成字符串
x = 'EA' #因为前一步已经把小写替换成大写了
y = [] #[]列表
for i in t:
    if i.find(x)<1: # 这个if语句不是太懂，暂时理解为找到含“EA”的单词就去掉
        y.append(i) # 把剩余的单词加入y
print(y)

print('\n') # 加了行空格
y.sort() #排序
print(y)