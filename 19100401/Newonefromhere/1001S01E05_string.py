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

#将text中的better全部替换成worse
text1=text.replace('better','worse')
#print(text1)

#替换text1中多余的符号
text1=text1.replace('\n',' ')
text1=text1.replace('*',' ')
text1=text1.replace('--','')
text1=text1.replace('!','')
text1=text1.replace(',','')
text1=text1.replace('.','')

#将text1中的文本分隔成单独的单词
text1=text1.split(' ')

#删除含有'ea'的单词
for i in range(len(text1)):
    if 'ea' in text1[i]:
        text1[i]=''

#将text1转换成str，将字母进行大小写翻转
text2=','.join(text1)
text3=text2.swapcase()

#去除空值，对结果进行排序
text4=text3.split(',')
text4=list(filter(None,text4))
text4.sort()
print(text4)