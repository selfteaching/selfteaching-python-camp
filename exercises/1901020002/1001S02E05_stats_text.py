sample_test = '''
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

#2.2 统计单词频次
elements = sample_test.split()
words = []
symbols = ',.*-' #剔除非单词
for element in elements:
    for symbol in symbols:
        element = element.replace(symbol,'')
    if len(element):
        words.append(element)
print('单词',words)
counter = {} #存放单词的次数
word_set = set(words) #去除重复元素
for word in word_set:
    counter[word] = words.count(word)
print('英文单词词频',counter)
#2.3 从大到小输出
print('从大到小输出单词及词频', sorted(counter.items(), key=lambda x：x[1],reverse=True))




