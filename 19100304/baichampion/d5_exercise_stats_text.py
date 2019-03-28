import collections              #导入一个收集？
import operator
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
text_0 = text.replace(',','').replace('.','').replace('--','')\
    .replace('!','').replace('*','').replace('\n','')
                                                                #通过replace整个方法将以上这些
                                                                #删除，但是换行不知怎删除。
text_1 = text_0.split(' ')                          #用split()将单词一空格分开
print(text_1)
text_2 = dict(collections.Counter(text_1))              #这里调用了一个计数函数counter
                                                        #这里dict后面不能直接用{}，不然语法错误
                                                        #现在dict只是作为一个函数被调用
print(sorted(text_2.items(),key=lambda x:x[1],reverse=True))    #不是很理解，以后再反复看？