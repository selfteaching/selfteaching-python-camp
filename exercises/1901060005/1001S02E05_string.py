text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''

t1 = text.replace('better','worse')#将字符串中的单词替换
t2 = t1.split()#以空格为分隔符，返回字符串列表。
t3 = []
for a in t2:
    if 'ea' not in a:
        t3.append(a)#添加没有‘ea’的单词
       # print (t3)
print(" ".join(t3))#将列表转化为字符串

t4 = ((" ".join(t3)).swapcase())#将列表转化字符串.jion(),并大小写翻转.swapcase()
#t5=sorted(t4,key=str.lower)
print (sorted(t4,key=str.lower))#字符串的单词按序列排列    