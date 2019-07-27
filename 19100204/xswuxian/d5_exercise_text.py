s= """
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
"""
s=s.replace('.',' ').replace(',',' ').replace('!',' ').replace('--',' ').replace('*',' ')#把非英文字符替换为空格
s=s.lower()#把所有单词变为小写
s=s.split()#以空格拆分为独立单词

dic={}
for i in s:  #将字符串转换为字典
    count=s.count(i)
    r1={i:count}
    dic.update(r1)
    #print(i,'',count )
print(dic)

print(end='\n')
print("按出现次数从大到小排列")
dic1=sorted(dic.items(),key=lambda x:x[1],reverse=True) #按照单词出现次数，从大到小排序
print(dic1)