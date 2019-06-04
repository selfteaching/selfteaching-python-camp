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
#在一开始用text的功能进行大小写转换
text=text.swapcase()

mytext = text.split( ) #将text拆分成一个个单词

#问题1，将包含ea的单词删掉

str1 = "EA"
newtext=[]
for i in mytext:
    if i.find(str1) < 0:  
       newtext.append(i)
#问题2,将better换为worse
for i in newtext:
    if i == 'better':
        newtext.insert(newtext.index(i),'worse')
        newtext.pop(newtext.index(i))       

newtext.sort() #对字符串排序
#将拆分的单词合并
lasttext=' '.join(newtext)
#打印输出结果
print(lasttext) 