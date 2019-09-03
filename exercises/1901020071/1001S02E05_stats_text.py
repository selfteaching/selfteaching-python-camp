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

#把字符串中的换行符替换为空，！替换为空，而.替换为空格
str1=text.replace("\n","").replace("."," ").replace("!","").replace("--","")
print(str1)
#按空格分隔
#print(list(str1))

print()
list1=str1.split(" ")
print(list1)

#创建一个空字典
hashmap={}
for ss in list1:
    #获取字典中对应的key的value值，如果没有，则设置为0
    count=hashmap.get(ss,0)
    hashmap[ss]=count+1

print(hashmap)

#按照出现次数从大到小输出所有的单词及出现的次数

# hashmap.items() 转为可迭代的列表； lambda表达式  
list2=sorted(hashmap.items(),key=lambda item:item[1])
print(dict(list2))

#只统计英文单词
str2=text.replace("\n","").replace("."," ").replace("!","").replace("--","")
dic={}
for ss in list1:
    #获取字典中对应的key的value值，如果没有，则设置为0
    count=dic.get(ss,0)
    dic[ss]=count+1

print(dic)


