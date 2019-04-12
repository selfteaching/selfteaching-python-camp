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

# 作业1 把text的better替换成worse
t1=text.replace('better', 'worse')     # replace是替代的意思，replace（'A','B'）就是把A替换成B
# print(t1)    #好，第一步是正确的

# 作业2  把text1中的ea剔除
t2=t1.split()    #这一步是把文章中的每个单词都分开
# print(t2)

#这个是参考了sunny老师辅导一个学员shannoxu

t3 = []
for a in t2:
     if 'ea' not in a:
        t3.append(a)

# print(t3)

# 作业3是要求把t3文本把大写变成小写，小写变成大写
# s.swapcase()可以用这个
# m="shosoousouusousufu"
# j=m.swapcase()
# print(j)    这个我看看他的功能


t4=' '
t5=t4.join(t3)
# print(t5)     #刚刚大哥说了，swapcase是针对字符串的，我要先把他之前列表的，变会字符串

t6=t5.swapcase()
# print(t6)

# 把t6按照从a到z  升序排列
t7=t6.split()
# print(t7)    #再变成列表先

t8=sorted(t7)
print(t8)





















