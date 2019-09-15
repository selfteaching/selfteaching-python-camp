sample_text = '''
the Zen of Python, by Tim Peters

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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

elements = sample_text.split()#将sample_text分割为字符集合
words = []#设置字符列表
symbols = ',.*-!'#定义非字母符号
for element in elements:#遍历字符集合
    for symbol in symbols:
        element = element.replace(symbol,'')#用空格代替非字母符号
    if len(element):#如果字符串长度>=1
        words.append(element)#把字符串放到列表中
print('正常的英文单词==>',words)

counter = {}#设置词典
word_set = set(words)#创建无序不重复元素集

for word in word_set:
    counter[word] = words.count(word)
print('英文单词出现次数 ==>',counter)

print('从大到小输出所有单词出现的次数 ==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))