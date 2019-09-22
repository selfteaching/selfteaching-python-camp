text='''
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

#str.replace(better,worse[,count]) 用worse替换better，count是可选的，表示替换的个数，默认全部替换
text1=text.replace('better','worse')

list=text1.split() #用str，split(sep=none，maxsplit=-1)函数将text1中的全部字符串拆分成一个个元素，返回成一个列表
list1=[]            #将一个空列表赋值给变量list1
for i in list:      #遍历循环
   if "ea" not in i:
      list1.append(i)  #如果“ea”不在此元素中的话，就把他假如到list1这个列表中，否则就continue进入下一个循环
   else:
      continue

a=" "
text2=a.join(list1)    #join()接受了list1里面的参数，并以字符串的形式拼接起来

text3=text2.swapcase()  #大小写转换
 
print(sorted(text3.split()))

 