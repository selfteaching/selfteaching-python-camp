text = '''
The Zen of python,by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Comples is better than complicated.
Flat is better than dense.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it may be a good idea.
If the implementation is easy to explain,it may be a good idea.
Namespaces are one honking great idea--let's do more of those!
'''


#print('1.2 将batter 全部替换成 worse'）
#print('1.3将替换后包含ea的单词剔除')
#print('1.4将上述结果所有字母大写变成小写，小写变成大写')
#print('1.5将以上结果按a-z升序排列') 

string=text.replace('''better''','''worse''')
string1=[] 
string2=[]      
for x in string.split():
        if x.find('ea') < 0:           
                string1.append(x)   
for x in string1:
    string2.append(x.swapcase()) 
string2.sort()
print(string2)



