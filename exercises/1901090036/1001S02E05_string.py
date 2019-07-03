text='''
The Zen of Python,by Tim Peters


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
In the face of ambxiguity,refuse the temptation to guess.
There should be one--and preferably only one--obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is haed to explanin,it's a bad idea.
If the implementation is easy to explanin, it may be a good idea.
Namespaces are one honking great idea--Let's do more of those!'''

print(text.replace('better','worse'))

x=text.replace('*','').replace('--','').replace('!','').replace('.','').replace(',','') #替换非英文字符

y=x.split()  #将文本中的单词转换为一个个元素
str1="ea"
str2=[] #使用一对方括号表示列表
for i in y:
    if str1 not in i:
        str2.append(i)
print(str2)
str3=('  '.join(str2)) # 将序列的元素连接生成新的字符串
print(str3)

o=text.swapcase() #大小写转换
print(o)

str2.sort()
print(str2)
