'''
string 
time：2019年7月18日21:08:36
version:1.0
'''
text ='''
The Zen of Python, by Tim Peters


Beautiful is better than guly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although particality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one -- and preferably only one -- obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's may be a good idea.
Namespace are one honking great idea -- let's do more of those!
'''

#1.字符串替换
text = text.replace('better', 'worse')
print('将better替换成worse后的text：',text)

#2.删除特定字符
#思路：将text切片，然后遍历一遍要删除的内容，剔除后重组

words = text.split()
filtered = [] #定义一个空的list用来存放过滤后的word
for word in words:
    if word.find('ea') < 0:
        filtered.append(word)
print('剔除ea后的text==>',filtered)
#回顾：1、切片；2、find命令；3、append命令

#3.大小写反转
#思路：直接利用str的大小写转换命令
'''print (type(filtered))
'''
reverse = [i.swapcase() for i in filtered]
print('大小写反转后==>',reverse)
#回顾：swapcase命令是str的，filtered的类型为list,无swapcase命令。

#4.将所有单词按照a到z的顺序排列
queuing = [sorted(reverse)]
print('将单词按a...z顺序排列后==>',queuing)