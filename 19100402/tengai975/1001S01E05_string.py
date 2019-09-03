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
#将字符串样本里的text里的better全部替换成worse
#用字符串本身的replace方法
text1=text.replace('better','worse')  #定义text1为新字符串，将字符串里的better全部替换成worse
print(text1)  #运行text1                    



#检索带有字母“ea”的单词并删除，形成新的list
list1=text1.split() #转换为列表
list2=[]
#遍历列表并去除含义‘ea’的单词
for i in list1:
    if 'ea'not in i:
        list2.append(i)
        print(list2)    

#字母大小的转换
text2="".join(list2)  #定义text2为join（）函数
text3=text2.swapcase()   #定义text3为text2的大小字母转换
print(text3) #运行text3 

#将text3的所有单词按a...z升序排列，并输出结果
list3=[]    #创建列表3为空列表
for i in list2:  #在列表2中循环i
        if i.isupper():  #如果 检索字符串
                list3.append(i.lower())#将列表中的所有大写字母转换为小写字母
        elif i.islower():
                list3.append(i.upper())
list3.sort()  #列表3按字母升序排列
print(list3)   #运行列表3             
