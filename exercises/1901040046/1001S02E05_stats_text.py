#将字符串s按照None的分隔切分为一个字符串组，并清洗字符串元素的标点符号
def cut_and_clean(s):
    #切分字符串
    s=s.split()
    #清洗标点符号
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.')
        if s[i]=='': #清洗完成之后若为空元素‘’，则删除元素
            s.remove('')
        else:
            i=i+1
    return s

#把list转化为dict并统计词频
def list_to_dict_and_cal(aList):
    aDict={}
    for i in range(len(aList)): #把list转化dict
        aDict[aList[i]]=0
    for i in range(len(aList)): #统计词频
        aDict[aList[i]]=aDict[aList[i]]+1
    return aDict

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

text = cut_and_clean(text) #切分字符串并清洗标点符号
text_dict = list_to_dict_and_cal(text) #将text转化为字典并统计词频
#对字典按照value值排序
#参考网页：https://www.cnblogs.com/dylan-wu/p/6041465.html
text_dict = sorted(text_dict.items(),key=lambda item:item[1],reverse=True)
print(text_dict)