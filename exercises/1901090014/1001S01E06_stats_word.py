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
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#去除符号
a=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
#print (a)
a=a.split() # 切割字符串  
#print(a)
def stats_text_en(a):   #定义函数
    import collections  #引用collections包
    c=collections.Counter(a)  #Counter 确定次数
    return c            #返回值

print(stats_text_en(a))  #使用函数


text1='化肥会挥发,黑化肥发灰,灰化肥发黑.黑化肥发灰会挥发 化发化黑'
x=text1.replace(',',' ').replace('.',' ')#去除符号
print(x)
def stats_text_cn(x): #定义函数
    j={}
    for i in x :                    #通过循环统计汉字
        if '\u4e00' <= i <= '\u9fff' :
            j[i]=x.count(i)+1
        else:
            j[i]=x.count(i)
    return j
text2=stats_text_cn(text1)           #调用函数
text3=text2.items()                  #字典函数
text4=sorted(text3,key=lambda i:i[1],reverse=True)      #降序
print(text4)
