Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@echojce Sign out
10
20 92 selfteaching/selfteaching-python-camp
 Code  Issues 36  Pull requests 6  Projects 0  Wiki  Insights
selfteaching-python-camp/19100101/WangRui0802/d5_exercise_stats_text.py
@WangRui0802 WangRui0802 The fifth day
6f3145d 3 hours ago
62 lines (56 sloc)  2.24 KB
    

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

#将字符串s按照None的分隔切分为一个字符串组，并清洗字符串元素的标点符号
def cut_and_clean(s):
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.!')
        if s[i]=='': 
            s.remove('')
        else:
            i=i+1
    return s

#把list转化为dict并统计词频
def list_to_dict_and_cal(aList):
    aDict={}
    for i in range(len(aList)): 
        aDict[aList[i]]=0
    for i in range(len(aList)): 
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
text_dict = sorted(text_dict.items(),key=lambda item:item[1],reverse=True)
print(text_dict)
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About