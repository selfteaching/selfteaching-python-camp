text='''
The Zen of Python,by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enoough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation to guess.
There shoule be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it's a bad idea.
If the implementation is easy to explain,it may be a good idea.
Namespaces are one honking great idea--let's do more of those!
'''

print(text.replace('better','worse')) #替换

x=text.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','') #替换非英文符号

y=x.split() #将单词转换为元素
str1='ea'
str2=[] #创建方括号代表列表
for i in y:
        if str1 not in i:
                str2.append(i)
print(str2)

str3=('  '.join(str2)) #将序列元素连接生成新的字符串
print(str3)

z=text.swapcase() #大小写转换
print(z)

str2.sort() #排序
print(str2)