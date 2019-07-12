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
t1=text.replace('better','worse')
#print(t1)  把better替换成worse并打印

t1=t1.replace(',','').replace('--','').replace('.','').replace('*','').replace('!','')#去除不相关元素
t2 = t1.split() #读取t1的字符串，并且转化成列表形式

t3=[] #创建一个空列表t3
for i in t2:  
        if 'ea' not in i :   #如果i的单词不包含‘ea’
                t3.append(i) #就把这个单词加入道t3
print(t3)                    

t4=[]                        #创建空列表t4
for i in t3:
        t4.append(i.swapcase()) #把t3列表当中的每个单词的字母一次进行翻转，并把翻转后的单词放入到t4
print(sorted(t4))               #按照字母进行排序，并打印。
       
    

    


