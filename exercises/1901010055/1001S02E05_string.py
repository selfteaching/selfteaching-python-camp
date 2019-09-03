text= '''
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
text = text.replace('better','worse')
print(text)
list = text.split( ) #拆分text字符串赋值给list。split()当不带参数时，以空格进行分割，并返回分割后的字符串列表（list）
str1=[]               #[] 创建新的空列表
for i in list:        # 遍历循环list
    if 'ea' not in i: #如果单词不包含ea，则进入str1
        str1.append(i)
    else:
        pass 
str2=" ".join(str1) #join()转化为字符串。str.join(元组、列表、字典、字符串) 之后生成的只能是字符串。
print(str2)
str3=str2.swapcase() #swapcase() 方法用于对字符串的大小写字母进行转换。
print(sorted(str3.split())) #split( )返回分割后的字符串列表，sorted(list)，sorted()不会改变原来的list，而是会返回一个新的已经排序好的list
                            #该函数也含有reverse这个bool类型的参数，当reverse=False时：为正向排序(从小到大)，默认为False。