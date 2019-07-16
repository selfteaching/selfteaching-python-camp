import re

text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!
'''

# 直接搜索python 字符串替换，可以找到replace函数
# replace函数并不会改变原text，替换后的值需要用另一个变量text2保存起来
text2 = text.replace('better','worse')
print(text2)

# 问题：删除所有包含ea的单词
# 搜索python  字符串剔除，找到strip，但是只能剔除空白字符
# 没有找到可直接解决问题的函数。看到关键词，正则表达式。
# 想到处理办法：1）通过正则表达式，匹配找到所有包含有ea的单词
#              2）删除这些单词
# 搜索正则表达式
# 1）含有ea的单词：  *ea*    
#    re.compile(r'*ea*')  报错
# 2）看到匹配单词的用法：\b\b
#    尝试含有ea的单词： \b*ea*\b
#    eaword = re.compile('\b*ea*\b')
#    text3 = eaword.search(text2)
#    print(text3)
#    依然失败

#打算请教。刚准备问问题时，想到有参考视频。解决问题。

# 1. Split a string into a list where each word is a list item
words = text2.split()
print(words) 

# 2. 遍历list，将不含有ea的单词保存起来
filtered = []
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print("将含有ea的单词剔除==>",filtered)
for word in filtered:
    print(word,end=' ')

# 问题： 大小写翻转
# 从教学视频看到swapcase函数
# 下面这行代码看得出python确实优雅
swapcased = [i.swapcase() for i in filtered]

# 问题：排序输出
print('按a...z降序排列',sorted(swapcased,reverse=True))
