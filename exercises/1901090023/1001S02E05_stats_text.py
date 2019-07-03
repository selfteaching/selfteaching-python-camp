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

for x in text.split():       # 将text中的文本以空格切分为一个数组，遍历这个数组
    y = x.strip(' --,.*!')    # strip()函数去掉text中所有特殊符号，只保留各个单词，y就等于列表中的每个单词
    print(y)
    
    if y not in d:           # 如果字典d中不存在这个元素，则将该元素作为key，存放在这个数组里，value初始化为1
        d[y]=1               
    else:
        d[y]=d[y]+1          # 如果字典d中存在此元素，则将这个元素对应出现的次数（value）取出来加上一次再放回去
print('每个单词以及出现次数')
print(d)                     # d的倒数第4个元素是('':1)，这是因为字符串中的最下行的“--”被认为是空字符串。

print('按出现次数降序输出')
print(sorted(d.items(),key=lambda d:d[1],reverse=True))     # items() 函数以列表返回可遍历的(键, 值) 元组数组；
                                                            # sorted()函数，通过key参数，指定第二个字段（value值）的值的降序来排序。


