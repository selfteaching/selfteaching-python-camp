#1.使用字典统计text中每个单词出现的次数
#2.按照出现次数从大到小输出所有单词及出现次数
#3.只统计英文单词
#Date:3/22/2019

#将字符串按照None的分隔切分为一个字符串组，并清洗字符串中的标点符号
def cut_and_clean(text):
    #切分字符串
    text=text.split()
    #清洗标点符号
    i=0
    while i<len(text):
        text[i]=text[i].split('*-.!')
        if text[i]=='':
            text.remove()
        else:
            i=i+1
    return text

#将字符串转化为dictionary并统计单词频率
def list_to_dict_and_count(aList):
    aDict={}
    for i in range(len(aList)):
        aDict[aList[i]]=0
    for i in range(len(aList)):
        aDict[aList[i]]=aDict[aList[i]]+1
    return aDict

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
text = cut_and_clean(text)
text_dict = list_to_dict_and_count(text)
text_dict = sorted(text_dict.items(),key=lambda item:item[1],reverse=True)
print(text_dict)


