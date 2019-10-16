
# 字符串串的基本处理理
Sample_text = '''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#1 将字符串串样本 text ⾥里里的 better 全部替换成 worse
text = Sample_text.replace('better','worse')
print ('将字符串中所有”better“替换成”worse"', text)

#2 从第 2 步的结果⾥里里，将单词中包含 ea 的单词剔除
words = text.split()
# print (words)
filtered_words = []
for word in words:
    if word.find('ea') < 0:
        filtered_words.append(word)
print('剔除包含ea的单词后的字符串', filtered_words)

#3 将第3步的结果⾥里里的字⺟母进⾏⼤⼩写翻转
switched_words = []
for word in filtered_words:
    switched_words.append(word.swapcase())
print('将大小写翻转后结果', switched_words)

#4 将第4步的结果⾥所有单词按 a…z 升序排列列
print('按 a…z升序排列', sorted(switched_words))
#print('按 a…z升序排列', sorted(switched_words, reverse=True))
