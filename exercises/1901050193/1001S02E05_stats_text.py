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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
words = text.split()#将字符串分隔构成list
wordlist = [] #建立存储用空单词list
symbols = ',.*-!' #各种符号构成的str
for word in words:#遍历list
    for symbol in symbols:#遍历各种符号
        word = word.replace(symbol,'')#替换掉符号
    if len(word):                      #那word是什么，list吗？list中的list?以及下面的singleword算什么呢。
        wordlist.append(word)
counter = {} #建立空字典
wordset = set(wordlist) #单词集合

for singleword in wordlist:
    counter[singleword] = wordlist.count(singleword)

print('计数：',counter)

#应用函数 counter.items()来返回key->value列表，还有lambda函数 进行排序
print('按出现次数降序排列:', sorted(counter.items(), key=lambda x: x[1], reverse=True)) 