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
Namespaces are one honking great idea -- let's do more of those! '''

text1 = text.replace('better','worse')
print(text1)
###################

text2 = text1.split()
text3 = text2[:] #分片拷贝，和直接赋值“=” 不同
for word in text2:
    if "ea" in word:
        text3.remove(word) #test3 移除有ea的单词
text2 = ' '.join(text3) #list 字符串化
text3 = text2.swapcase()#字符串转换大小写
text3 = text3.split()
text3.sort()#排序
print(text3)


