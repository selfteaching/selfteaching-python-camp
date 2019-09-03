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
#将better全部替换成worse
str1 = text.replace('better','worse')
#print(str1)


#删除含ea的单词
str2 = str1.split()  #把字符串变成list
str3 = [x for x in str2 if 'ea' not in x]

#大小写翻转
str4 = " ".join(str3) #把list变回字符串
str5 = str4.swapcase()

#按照a-z升序排列
str6 = str5.split() #变回list
str6.sort( )
print(str6)