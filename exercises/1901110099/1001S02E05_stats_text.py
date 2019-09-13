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

text1=text.replace(',','').replace('.','').replace('--','').replace('*','').replace('!','')
text2=text1.split()
dict1={}
for letter in text2:
    if letter in dict1:
        dict1[letter]=dict1[letter]+1
    else:
        dict1[letter]=1
print(dict1)

print()
print('按照出现次数从大到小输出所有的单词及出现的次数')
print(sorted(dict1.items(),key = lambda x:x[1],reverse = True)) 






    







  
