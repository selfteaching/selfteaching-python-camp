sample_text='''
The Zen of Python,by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren`t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation tu guess.
There should be one--and preferably only one--obvious way to do it.
Although that way may not be obvious at fitst unless you`re Dutch.
NOw is better than never.
Although never is often bettet than*right*now.
If zhe implementation is hard to explan,it`s a bad idea.
If zhe implementation is easy to explan,it may be a good idea.
Namesoaces are one honking great idea--let`s do more of those!
'''

elements=sample_text.split()
words=[]
symbols=',.*-!'
for element in elements:
    for symbol in symbols:
        element=element.replace(symbol,'')
    if len(element):
     words.append(element)
print('英文单词=====',words)
counter={}
word_set=set(words)
for word in word_set:
    counter[word]=words.count(word)
print('单词出现次数===',counter)
print('按大小排列次数===',sorted(counter.items(),key=lambda x: x[1],reverse=True))