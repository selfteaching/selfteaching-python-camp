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

# 1.替换掉所有的符号
word_str = text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')
# print(word_str)

# 2.按照空格将所有的单词分割开
word_list = word_str.split()
# print(word_list)

# 3.对单词进行去重操作，作为字典的key
word_one = set(word_list)
# print(word_one)

# 4.构建一个词频字典
dict = {}
for word in word_one:
    dict[word] = word_list.count(word)

# 5.对之前的词频字典按照value值进行排序
d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
new_dict = {}
for item in d_list:
    new_dict[item[0]] = item[1]
# print(d_list)

# 6.输出，检查结果
print(new_dict)