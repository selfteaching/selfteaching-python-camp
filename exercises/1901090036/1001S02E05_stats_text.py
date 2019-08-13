text='''
The Zen of Python,by Tim Peters


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
In the face of ambxiguity,refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it's a bad idea.
If the implementation is easy to explain,it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
x=text.replace(',','').replace('.','').replace('!','').replace ('*','').replace('--','')

y=x.split() #拆分字符串，以单词为单位进行统计，拆分后变成列表
dict={} #创建字典
for i in y:
    j=y.count(i) #i在y中出现的总次数
    dict2={i:j} #i到j的切片
    dict.update(dict2) #update()函数把字典dict2的键/值更新到dict
    print(dict2)
    print('\n')

dict3=sorted(dict.items(),key=lambda x:x[1],reverse=True) #items()函数将字典转化为元组，遍历键/值，x:x[]字母可以随意修改，表示选取第二个元素做比较 reverse表示降序
print(dict3)