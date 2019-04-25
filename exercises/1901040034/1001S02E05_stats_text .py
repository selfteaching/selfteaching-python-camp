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

T1=text.replace(',','').replace('.','').replace('--','').replace('!','').replace('*','')
T1=T1.split()
T2=[]
for x in T1:
        if x.isalpha:
                T2.append(x)        
print(T2)

dict={}
for x in T2:
        y = T2.count(x)
        dict1 = {x:y}
        dict.update(dict1)
print(dict)

dict2=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(dict2)



    



 











