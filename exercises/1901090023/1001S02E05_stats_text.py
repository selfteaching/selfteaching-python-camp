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

# 2. 统计字符串样本中英文单词出现的次数

d={}                         #创建一个空字典

for x in text.split():       # x 是列表中的一切单词元素，包括在一起的特殊符号
    y = x.strip(' -,.*!')    # strip()函数去掉text中所有特殊符号，只保留各个单词，y就等于列表中的每个单词
    print(y)
    
    if y not in d:           # 34-37行代码看不懂，想不明白。
        d[y]=1
    else:
        d[y]=d[y]+1
print('每个单词以及出现次数')
print(d)                     # 问题是，d的倒数第4个元素是('':1)，这点不懂。因为前面的y里应该去掉空格了。

print('按出现次数降序输出')
print(sorted(d.items(),key=lambda d:d[1],reverse=True))     # items() 函数以列表返回可遍历的(键, 值) 元组数组；
                                                            # sorted()函数，通过key参数，指定第二个字段（value值）的值的降序来排序。


