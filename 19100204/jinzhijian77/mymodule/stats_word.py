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


import re
import collections
import jieba

dict1 = {}
str1 = ''

count = int
count = 5



def stats_text_en(text,count):  #define the function 

    

    text = re.sub("[^A-Za-z]", " ", text.strip())  #only keep Eng, from the same reference 

    list1 = re.split(r"\W+",text)   #text to list1 

    

    while '' in list1:   

        list1.remove('')  #delete space 
    return collections.Counter(list1).most_common(count)







def stats_text_cn(text,count): #define a function to calcuate character frequencies 



    text = re.sub("[A-Za-z]", "", text) #only keep chinese and numbers



    list1 = re.split(r"\W+",text)   #use list 1 in the previous section 



    while '' in list1:   

        list1.remove('') #delete space 
    str1 = ''.join(list1)

    seg_list =[ x for x in jieba.cut(str1,cut_all=False) if len(x) >= 2]

    return collections.Counter(seg_list).most_common(count)



def stats_text(text,count):

    return collections.OrderedDict(collections.Counter(stats_text_en(text,count)+stats_text_cn(text,count)))


