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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# https://blog.csdn.net/jiaowosiye/article/details/79209422

#去掉标点符号、连接符、！、*
aa = text.replace(","," ").replace("."," ").replace("--"," ").replace("!"," ").replace("*"," ").replace("\n","")
new = aa.split(" ") #分割字符串，变为列表,以空格进行分割。


print("统计单词出现次数：")
d ={} #这里要用大括号
for i in new :          
    j= new.count(i)     # 一个元素出现的: 次数 ,此处的i 就表示一个单词,上面已经分割好;另外用法 也可以是一个字符串中的 某一个或者几个字母,比如 'ea'
    d[i] = j # 这里就是把这个单词 和 出现的次数 添加到 字典中,当然也可以用 update 函数 
    #   d={i:j} #这里要用大括号
d.pop("")
print(d)


print("按出现频次数从大到小输出：")  
# sorted 函数 排序:https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto
d1=sorted(d.items(),key=lambda x:x[1],reverse=True)   
print(d1) 


""" 
扩展用法 : <<对于sorted key键 排序还是不熟悉 ,多看资料加强 >>

在Sorting Keys中：我们看到，此时排序过的L是仅仅按照第二个关键字来排的，如果我们想用第二个关键字
排过序后再用第一个关键字进行排序呢?
>>> L = [('d',2),('a',4),('b',3),('c',2)]
>>> print sorted(L, key=lambda x:(x[1],x[0]))
>>>[('c', 2), ('d', 2), ('b', 3), ('a', 4)] 
"""

