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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 替换
text1 = text.replace('better', 'worse')
#print(text1)

# 先转换成列表，然后进行删除操作，再转换成字符串
list1 = text1.split()
i = 0
while i < len(list1):
    if 'ea' in list1[i]:
        del list1[i]
    i += 1
text2 = " ".join(list1)
#print(text2)

# 大小写反转
text3 = text2.swapcase()
#print(text3)

# 先将字符串转成列表，再升序排列
list2 = text3.split()
list2.sort()
print('输出结果：')
print(" ".join(list2))