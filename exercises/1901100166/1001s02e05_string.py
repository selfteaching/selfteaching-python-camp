a = '''
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

#1.将字符串样本里的 better 全部替换成 worse

# 调用 str 类型 的 replace 方法进行替换
b= a.replace('better','worse')
#print('将字符串样本里的 better 全部替换成 worse ==>', b)

#2.
c=a.split()   #调用str类型，将字符串 根据 空白字符 分割成list
guolv=[]       #定义list类型的变量存放过滤后的单词
for d in c:       #句型判断是否含ea
    if d.find('ea')<2:  # str类型的find方法 不含参数则返回-1，含则返回第一次出现的索引
        guolv.append(d)
print('剔除ea',guolv)

#3.大小写翻转
E=[e.swapcase() for e in guolv]
#print('333333',E)

#4.单词升序排列
#print('升序==>',sorted(E))  #sorted默认升序

#print('降序==>',sorted(E, reverse=True))





