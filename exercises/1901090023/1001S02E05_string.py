text = ''' 
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

# 1. 字符串的基本处理
print('样本中better全部替换为worse')
print(text.replace('better', 'worse'))                    # better 替换成 worse

text1=text.replace('better', 'worse')                     # 1.2步后的text, 命名为text1
text2=text1.split()                                       # 用str.split()方法把字符串变成由若干个元素组成的列表，命名为text2
text3=[]                                                  # text3初始为空列表

for x in text2:                                           # x 为 列表text2中的任意元素（字符串）
    if 'ea' not in x:                                     # 在列表中删除包含ea的单词
        text3.append(x)                                   # text3 为不包含ea的单词的列表
print(text3)                                              # text3创建一个空列表，下面的for循环是把不包含ea的单词找出来并添加到text3中，print要与text3对齐。如果往右4或8个空格，是在for循坏内，打印会报错。

text4=(' '.join(text3))                                   # 把text3列表中各个元素连接生成新的字符串，每个元素之间用空格相连
text5=text4.swapcase()                                    # 把text4字符串中的单词进行大小写翻转，生成text5字符串
print('删除ea单词以及大小写翻转后的字符串')
print(text5)                                              

text6=text5.split()                                       # text5由字符串变成列表text6
print('按单词字母升序排列')
print(sorted(text6, key=str.lower))                       # 将text6列表中的每个元素变为小写，再按每个元素中的每个字母的ascii码从小到大排序 


# sorted("This is a test string from Andrew".split(), key=str.lower)   # 关于Key函数用法，可以参考一下例子
# 输出结果：['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']