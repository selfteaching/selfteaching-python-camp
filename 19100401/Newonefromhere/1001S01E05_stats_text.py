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

#删除text中除英文单词外所有符号
text1=text.replace('\n',' ')
text1=text1.replace('*',' ')
text1=text1.replace('--','')
text1=text1.replace('!','')
text1=text1.replace(',','')
text1=text1.replace('.','')
text1=text1.split(' ')

#去除空值
text1=list(filter(None,text1))

#统计单词出现次数
dic={}
for i in text1:
    dic.update({i:text1.count(i)})

#按照出现次数，从大到小排列
dic2=sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(dic2) 