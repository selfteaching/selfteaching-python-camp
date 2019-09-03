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
RRs_str=[]
for x in T1:#遍历字符串 去除所有的\n或者\t
        if x.isalpha:
                RRs_str.append(x)
print(RRs_str)

dir1 = {}
for i in RRs_str:#遍历列表
    if i in dir1:#如果key值出现过，相应的value值就+1
        dir1[i]+=1
    else:
        dir1[i]=1
print(dir1)
print('==========第2步========')

dir1=sorted(dir1.items(),key=lambda x:x[1],reverse=True)#将key值和value值排序
print(dir1)
print('===========第3步=======')
