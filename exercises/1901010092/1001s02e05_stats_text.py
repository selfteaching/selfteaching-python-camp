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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#使用字典 统计单词出现次数
 
a1=text.replace("*"," ").replace("-"," ").replace(","," ").replace("."," ").replace("--"," ").replace("!"," ")
a1=a1.split()
i=0
dictData = {}
for word in a1:
    i = a1.count(word)
    dictData[word] = i


#按照从大到小输入所有的单词及出现的次数
dic2=sorted(dictData.items(),key = lambda item:item[1],reverse=True)

print(dic2)
