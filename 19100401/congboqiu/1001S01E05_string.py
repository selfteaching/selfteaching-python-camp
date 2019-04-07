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
print('2.将text里的better全部字符串替换worse')
text=text.replace('better','worse')#替换字符串
print(text)

text=text.swapcase() #大写字母转换成小写，小写字母转换成大写
print(text)

text=text.replace(',','').replace('.','').replace('*','').replace('--','').replace('!','')
print(text)      #把非英文符号替换为空格

text=text.split()#把text分片（此时的变量text已经分片为序列）
temp1='ea'       #定义字串为'ea'的temp1
temp2=[]         #定义序列为空的temp2
for x in text:         #for循环遍历text序列中的所有元素
    if x.find(temp1)<0:#x.find()的意思是查找匹配字串ea，没有找到，返回值为-1,
        temp2.append(x)#逻辑判断为true，执行下一条。其它的为false
                       #没有'ea'字串添加到序列temp2中
print(temp2)

temp2.sort()
print(temp2)
#text1=' '.join(temp2)
#text1=text1.split()
#text1.sort()#将所有单词按a...z的升序排列
#print(text1)
