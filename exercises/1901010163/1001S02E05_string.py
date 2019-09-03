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

# 将text中的better替换为worse
text_1 = text.replace('better', 'worse')
# print(text_1)

# 把text_1中含ea的单词剔除
words_1 = text_1.split()
# print(words_1)
words_2 = [word.strip(',.!*-') for word in words_1]
words_2.remove('')
# print(words_2)
words_3 = [word for word in words_2 if 'ea' not in word]
# print(words_3)

# 把words_3中的字母进行大小写翻转
words_4 = [word.swapcase() for word in words_3]
# print(words_4)

# 把所有单词升序排列，输出结果
words_4.sort(key=str.lower)
for word in words_4:
    print(word, end=' ')