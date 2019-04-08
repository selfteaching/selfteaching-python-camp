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
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数
symbol_deleting=[',','.','-','*','!']  #将标点符号替换为空格
for x in symbol_deleting:
    text=text.replace(x,'')  
text=text.lower()  #将所有单词变成小写
text=text.split()  #使字符串text变成列表
print(text)
type(text)

list2={x for x in text }
type(list2)

list3={}

for i in text :
    list3.update({i:text.count(i)})
print(list3)

list4=sorted(list.items(),key=lambda x:x[1],reverse=True)
print(list4)
