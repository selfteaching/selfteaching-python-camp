text='''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
 it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#把better替换成worse
t1 = text.replace('better','worse')
print("将所有better替换成worse==>",t1)
print("-------------------------------------------------------------------------------")

#删除字符串中的带ea的单词
l1 = text.strip().split()
l2 = []
for i in range(len(l1)):
    if l1[i].find('ea') == -1:
        l2.append(l1[i])

s1 = ' '.join(l2)

#大小写转换
s2 = s1.swapcase()
print(s2)
print('---------------------------------------------------------------------------------')

#按单词排序
s3 = s2.replace('*','').replace('.','').replace('-','').replace('!','').replace(',','')
l3 = s3.split()
l4 = sorted(l3)
print(sorted(l3))

print('----------------------------------')
s4 = ' '.join(l4)
print(s4)

#print(s3)
#l3 = []
#for a in s2.split(','):
#        for b in a.split():

#                l3.append(b.strip('*').strip('.').strip('-').strip('9').strip('!'))

#去掉列表中的空字符元素
#l4 = list(filter(None,l3))

#可以用 sort和sorted两种方法对列表元素排序
#方法1:sort函数
#l4.sort()
#s3 = ','.join(l4)
#print(s3)
#方法二：sorted函数
#print(sorted(l4))
