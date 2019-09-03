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
text1 = text.replace("better","worse")  #作业1替换better为worse
print(text1)

text2 = text1.split(" ") #字符串变为列表
list=[] #作业2删除有ea的单词
for i in text2:
   if 'ea' not in i:
       list.append(i) 
   else:
       continue #遍历列表test2中没有ea的word并打印
print(list)     

s=' '
str=s.join(list)#把列表变为字符串 


str1 =str.swapcase() #作业3替换大小写 
print(str1)
l2 = str1.split()#分割字符串为列表


l3 = sorted(l2)#作业4按照a-z排列
print(l3)
str2 = ' '
str3 = str2.join(l3) #把列表变回字符串
print(str3)