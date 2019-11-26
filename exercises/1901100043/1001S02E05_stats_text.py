text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!
'''

elements = text.split()

words = []

symbols = ',.*-!'

for e in elements:
    for s in symbols:
        e = e.replace(s,'')
    if len(e):
        words.append(e)

print('正常英语单词==>',words)

counter = {}

word_set = set(words)
for word in words:
    counter[word] = words.count(word)
print('英语单词频率==>',counter)

print('从小到大输出所有单词及出现次数==>',sorted(counter.items(),key=lambda x: x[1],reverse=True))


'''
7月14日完成练习
照着视频一步一步做的。
涉及到列表、元组、集合等数据类型，字符串处理，排序等函数，还有lambda语句。
这些概念，需要练习熟练。
'''