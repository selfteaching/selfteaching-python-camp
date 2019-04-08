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
str1=text.replace("better","worse")   #将better替换为worse
#删除含“ea"的字
str2=str1.split()
w1="ea"
w2=[]
for i in str2:
    if i.find(w1)<1:
        w2.append(i)
str3=" ".join(w2)
#字母进行大小写翻转
str4=str3.swapcase()
#排序
str5=str4.replace(","," ").replace("."," ").replace("--"," ").replace("!"," ").replace("*"," ")
str6=str5.split()
str7=sorted(str6)
str8= " ".join(str7)
print(str8)