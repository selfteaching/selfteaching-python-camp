text = '''
The Zen of python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced
In the face of ambxiguity,refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch
If the implementation is hard to explain,it's a bad idea
If the implementation is easy to explain,it's may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''
s = text.replace('better','worse')
print(s)

t =s.split(',')
print(t)

r = []
for i in t:
    if 'ea' not in t:
        r.append(i)
print(r)

r = [item.swapcase() for item in r]
print(r)

#将第四步的结果里所有单词按a~z升序排列，我的理解是：a开头的所有字母全部排前面，b开头的所有字母排a的后面，依次类推。
# 那先将大小写字母均先转换为小写，否则按照acsii码进行排序
#目前问题是 ，按下面的方法，无法实现全部都转换为小写，而且是字符串，不知如何切换为单个字母 。
r.sort()
print(r)