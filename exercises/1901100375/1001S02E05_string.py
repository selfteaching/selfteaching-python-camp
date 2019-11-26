# DAY5 掌握基本数据类型 2019-11-03

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
#Task1-1：字符串的基本处理-替换
textnew = text.replace('better','worse')
print(textnew)

#Task1-2：字符串的基本处理-去除
#首先是要找到含有ea的单词，要找到单词首先要用分割规律分割出每个单词（现在是每个单词后面有个空格）
#step1 分割
listnew = textnew.split( )
print(listnew)
#step2 把没有ea的增加到新的数列里面去
listnew2 = []
for i in listnew:
    if "ea" in i:
        pass
    else:
        listnew2.append(i)
#step3 转化成字符串
result = ""
for i in listnew2:
    result += i + " "
print(result)

#Task1-3：字符串的基本处理-进行⼤小写翻转
textnew2 = result.swapcase()
print(textnew2)

#Task1-4：#所有单词按a...z升序排列列，并输出结果
listnew3 = textnew2.split( )
listnew3.sort()
print('\n单词首字母按a-z升序后新列表text5如下：\n',listnew3)
