a="The Zen of Python, by Tim Peters Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
#str.count(sub[,start=The,[end=those]])
dict={'song':'123','qihong':'666'}
print(dict['song'])#[]表示索引到song这个键，但是song是字符串所以要用''；print后面跟的是（）

#列表
#1，列表可以包含任何对象：数值，字符串，列表
m=range(10)#1--9
print(m)
for i in m:
    print(i)
print(m[2],m[-1],m[5])#m[2]1,2


txt = '''
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
#把better都替换成worse
txt2=txt.replace("better","worse")
print(txt2)
#单词里面包含ea的单词剔除：1.先找到包含ea的单词，2.删除该单词
#第一步找到ea的单词，这个是要让程序进去整个文档后挨个字符串的走一遍，所以先要把各个字符串分割开来
txt3=txt2.split()
#print(txt3)#打印试试看
#在列表中，用什么方法可以找到固定的目标呢？百度一下：有个方法叫.find
file=[]#新建一个仓库，一旦没有ea的单词，就把它们放进去
for word in txt3:#把txt4放进字符串txt3中走一遍
    if word.find('ea')<0:#当txt4没发现字符串中含有ea的话
        file.append(word)#就把txt4正在经历的这个字符串增加到file这个列表中
print(file)

#将第 3 步的结果⾥里里的字⺟母进⾏行行⼤大⼩小写翻转（将⼤大写字⺟母转成⼩小写，⼩小写字⺟母转成⼤大写)
#1得先把file字符串中的元素变成列表，然后再转化
lst=[i.swapcase() for i in file]#i这个变量全都变成大写的方法.swapcase（意思是i这个变量要大写）；把i放到file里面走一遍
print(lst)#打印i

#用sorted这个函数
print(sorted(lst))