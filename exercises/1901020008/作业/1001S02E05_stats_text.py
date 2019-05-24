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


string=text.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ').replace('.',' ')
string1=string.lower()
    #print(string1)
string2=string1.split()
#print(string2)
string3={}
for a in string2:
   count=text.count(a)
   text_count={a:count}
   string3.update(text_count)
#print(string3)

string3=sorted(string3.items(),key=lambda a:a[1],reverse=True)
print(string3)
