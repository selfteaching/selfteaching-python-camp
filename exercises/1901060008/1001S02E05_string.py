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
print('第一题：将字符串样本里的better全部换成worse\n')
t=text.replace('better','worse').replace(',','').replace('.','').replace('--','').replace('*','')   #首先替换题目要求的字符，然后把多余的标点符号去掉。
print(t)  
print('*'*50)
print('第二题：在第一题基础上，将单词带有ea的单词剔除\n')
t1=t.split()        #拆分字符串
#print(t)
del_ea=[]
for i in t1:
    if 'ea' not in i:
        del_ea.append(i)
print(del_ea)
print('*'*50)
print('第三题：在第二题的基础上，对字母进行大小写翻转\n')
t2=' '.join(del_ea)
print(t2)
t3=t2.swapcase()
print(t3)
print('*'*50)
print('第四题：在第三题的基础上把单词按a...z排序\n')
t4=t3.split()
t5=sorted(t4)
# print(t5)
t6='  '.join(t5)
print(t6)


