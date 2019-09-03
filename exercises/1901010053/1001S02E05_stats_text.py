 
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

text1=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#将非英文字符替换为空格
text2=text1.split()
dict={}
for i in text2:  
    j=text2.count(i) #统计单词i（变量）在text2中出现次数
    dict2={i:j}
    dict.update(dict2) # update() 函数把字典dict2的键/值对更新到dict里
dict3=sorted(dict.items(),key=lambda x:x[1],reverse=True) #dict.items()遍历（键/值）元祖数组，x:x[]字母可以随意修改，排序方式按照中括号[]里面的维度，[0]按照第一维，[1]按照第二维。reverse=True降序
print(dict3)