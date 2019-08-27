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
print(text)
print("使用字典（dict）统计字符串样本 text 中各个英文单词出现的次数。")
elements=text.split()
words=[]
symbols=",.*-!"

for element in elements:
    for symbol in symbols:
        element=element.replace(symbol,"")
    if len(element):
        words.append(element)

print("正常的英文单词：",words)

counter={}

#word_set=set(words)

for word in words:
    counter[word]=words.count(word)

print("英文出现的次数：",counter)

print("按照出现次数从⼤到⼩输出所有的单词及出现的次数")
'''
key=lambda 元素: 元素[字段索引]
比如   print(sorted(C, key=lambda x: x[2]))   
x:x[]字母可以随意修改，排序方式按照中括号[]里面的维度进行排序，[0]按照第一维排序，[2]按照第三维排序
'''
print(sorted(counter.items(),key=lambda x:x[1], reverse=True))