sample_text = '''
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

elements=sample_text.split()
words=[]
symbols='* . - ! ,'
for element in elements:
    for symbol in symbols:
        element=element.replace(symbol,'')   
    if len(element):     
        words.append(element)
print('正常的英文单词 ==>',words)

counter={} #定义一个字典集合

word_set=set(words)  #对words做一个集汇总，统计words中所有出现过的单词
for word in word_set:   #如果 Word 在 set的集合中
    counter[word]=words.count(word) #那么，统计这个单词出现的次数（用count（word）这个程序），并添加到 新的words命名的list，
               #然后赋值给 counter[word]
print('英文单词出现的次数 ==>',counter)  # counter print 出来的结果是 {'those': 1, 'Dutch': 1, 'may': 2, ....}

print('从大到小输出所有单词出现的次数 ==>',sorted(counter.items(), key=lambda X : X[1],reverse=True))