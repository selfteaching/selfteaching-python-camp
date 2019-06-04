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
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，
最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，
越来越多被用于独立的、大型项目的开发。'''

dict1 = {} #Decalre variable is blank 
dict2 = {}
dict3 = {}
dict4 = {}

def stats_text_en(text):  #define the function 
    import re # reference:https://docs.python.org/3/library/re.html 
    text = re.sub("[^A-Za-z]", " ", text.strip())  #only keep Eng, from the same reference 
    list1 = re.split(r"\W+",text)   #text to list1 
    
    while '' in list1:   
        list1.remove('')  #delete space 
    
    for i in list1:   #loop 
        
        dict1.setdefault(i,list1.count(i))  
   
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   #Arrange 

    for tup1 in tup1:   
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2

print("英文词频:") #printing funciton 
print(stats_text_en(text))


def histogram(s, old_d):
    d = old_d
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def stats_text_cn(text): #define a function to calcuate character frequencies 
    import re
    text = re.sub("[A-Za-z0-9]", "", text) #only keep chinese and numbers

    list1 = re.split(r"\W+",text)   #use list 1 in the previous section 

    while '' in list1:   
        list1.remove('') #delete space 

    dict3 = dict()        #use dict function
    
    for i in range(len(list1)):
        dict3 = histogram(list1[i], dict3)

    
    tup1 = sorted(dict3.items(),key = lambda items:items[1],reverse = True)  

    for tup1 in tup1:   
            dict4[tup1[0]] = dict3[tup1[0]]  
    return dict4

print("中文词频:")
print(stats_text_cn(text))
