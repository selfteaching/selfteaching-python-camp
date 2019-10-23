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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#print (f'{text}')
#text.capitalize()
#在一串字符串中，空格也算是一个字符串。如果字符串的开头是一个空格，此时我们会发现capitalize()方法返回的字符串全是小写，这是因为空格没有大小写之分，空格在第一个位置，其它字符串自然全是小写喽
#text.capitalize()
#print(f'{text.capitalize()}')


#print (text.count('ea'))
#better 字符串出现了8次



#####   1
#替换字符
#print(text.replace('better','worse'))
test1=text.replace('better','worse')
#print (test1)   #查看替换结果



######   2 去除含有ea的单词
#print(test1.split())    #把字符串以空格分开，显示出所有单词

text2=test1.split()
#print (text2)
text3=[]
for x in text2:
    if 'ea'   not in  x:
        text3.append(x)
#print(text3)


######## 3 将单词中的大写字母变为小写字母，小写字母变为大写字母

text4=' '.join(text3)    #把text3变量列表模式转换为字符串模式，新的字符串值为text4
#print (text4)

text5=text4.swapcase()   #大写字母变为小写字母，小写字母变为大写字母
#print (text5)



#######   4 把text5的所有单词按照a-z的顺序升序排列
text6=text5.split()
text6.sort(reverse = False)
print (text6)




