
sample_text="""
The zen of Python,by Tim peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it's a bad idea.
If the implementation is east to explain,it may  be a good idea.
Namespaces are one honking great idea-- let's do more of those!
"""

elements=sample_text.split()
words=[]
symbols=",.*-"
for element in elements:
    for symbol in symbols:
        element=element.replace("symbols","")
        if len(element):
            words.append(element)
print("打印正常的英文单词",words)

# 统计单词出现的次数
counter={}
word_set=set(words)
for word in word_set:
    counter[word]=words.count(word)
print("统计单词出现的次数",counter)
#按照出现次数从大到小统计所有的单词及出现的次数
print("按照出现次数从大到小统计所有的单词及出现的次数",sorted(counter.items(),key=lambda x:x[1],reverse=True))
