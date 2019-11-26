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

text = sample_text.replace('better','worse')
print('将字符串样本里的 better 全部替换成 worse ==>',text)

words=text.split()
filtered = []
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print('将单词中包含 ea 的单词剔除 ==>',filtered)

swapcased = [i.swapcase() for i in filtered]
print('进行大小写翻转 ==>', swapcased)

print('单词按 a…z 升序排列 ==>',sorted(swapcased))
