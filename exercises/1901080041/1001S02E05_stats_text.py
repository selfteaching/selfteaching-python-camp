text = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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

#使⽤用字典(dict)统计字符串样本text中各个英⽂文单词出现的次数
str1 = text.split()       #把字符串转化成单词
words = []                #定义一个list变量放处理好的单词
symbol = ',.-*!'          #需要去除的所有符号

for i in str1:
    for j in symbol:
        i = i.replace(j,'')   #把符号用空格替代剔除
    if len(i):                
        words.append(i)       #如果字符串长度不为零则为单词
print('无序单词：\n', words)

counter = {}    #定义一个dict变量放处理好的单词个数
words_set = set(words)    # 去重

for word in words_set:
    counter[word] = words.count(word)
print('单词出现次数：\n', counter)
print('降序排列：\n', sorted(counter.items(),key=lambda x:x[1],reverse=True))

        


    

