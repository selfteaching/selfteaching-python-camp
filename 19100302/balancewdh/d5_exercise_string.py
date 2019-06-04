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
There should be one—- and preferably only one —-obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#将better替换成worse
a = text.replace('better','worse')

#删除包含ea的单词
list1 = ''
list2 = ''
list3 = ''
list2 = list1.join(a)
import re
list3 = re.split(r"(\W+)",list2)
for i in list3:
    if 'ea' in i:
        list3.remove(i)

#翻转大小写
list4 = ''
list5 = ''
list6 = ''
list5 = list4.join(list3)
list6 = list5.swapcase()

#将单词按升序排列
b = re.split(r"\W+",list6)
b.sort()
while '' in b:
    b.remove('')
    print(b)