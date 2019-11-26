sample_text='''
2 The Zen of Python, by Tim Peters
3
4
5 Beautiful is better than ugly.
6 Explicit is better than implicit.
7 Simple is better than complex.
8 Complex is better than complicated. 9 Flat is better than nested.
10  Sparse is better than dense.
11  Readability counts.
12  Special cases aren't special enough to break the rules.
13  Although practicality beats purity.
14  Errors should never pass silently.
15  Unless explicitly silenced.
16  In the face of ambxiguity, refuse the temptation to guess.
17  There should be one-- and preferably only one --obvious way to do
    it.
18  Although that way may not be obvious at first unless you're Dutch.
19  Now is better than never.
20  Although never is often better than *right* now.
21  If the implementation is hard to explain, it's a bad idea.
22  If the implementation is easy to explain, it may be a good idea.
23  Namespaces are one honking great idea -- let's do more of those!
24  '''

elements = sample_text.split()
words = []
symbols = ',.*_!'
for element in elements:
    for symbol in symbols:
        element = element.replace(symbol,'')
    if len(element):
        words.append(element)
print('正常的英文单词 ==>',words)

counter = {}
word_set = set(words)
for word in word_set:
    counter[word] = words.count(word)
print('英文单词出现的次数 ==>',counter)
print('从大到小输出所有的单词及出现的次数 ==>',sorted(counter.items(),key=lambda x: x[1],reverse=True))