text = '''
The Zen of Python, by Tim Peters.
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

def cut_and_clean(s):
    s=s.split()
    i=0
    while i<len(s):
        s[i]=s[i].strip('*-.')
        if s[i]=='': 
            s.remove('')
        else:
            i=i+1
    return s

def list_to_dict_and_cal(aList):
    aDict={}
    for i in range(len(aList)): 
        aDict[aList[i]]=0
    for i in range(len(aList)): #统计词频
        aDict[aList[i]]=aDict[aList[i]]+1
    return aDict

text = cut_and_clean(text) 
text_dict = list_to_dict_and_cal(text) 
text_dict = sorted(text_dict.items(),key=lambda item:item[1],reverse=True)
print(text_dict)