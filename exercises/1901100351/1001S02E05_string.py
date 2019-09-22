text = '''
the Zen of Python, by Tim Peters

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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

t1=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ').replace('!',' ')
# 去掉文本中的中文字符、英文字符、字号、连接符
t2=t1.replace('better','worse')# 用worse替换better
print(t2)

t3=t2.split()# 以空格为分隔符，将t2中的字符串转换为列表
t4=[]# 将t4创建为列表，通过索引获取字符串中的字符
for a in t3:# 在t3中循环查找a（a代表所有字符串）
    if 'ea' not in a:# 如果ea不在字符串中
        t4.append(a)# 在t4后添加字符串（即把不含ea的字符串挑出来放在t4中）
print(t4)

t5=(' '.join(t4))# 用空格做分隔t4中的字符串，形成t5
t6=t5.swapcase()# 将t5中的大小写字母反转，形成t6
t7=t6.split()# 以空格为分隔符，将t6中的字符串切片，形成t7
print(sorted(t7,key=str.lower))#将t7中的字符串按字母升序排列