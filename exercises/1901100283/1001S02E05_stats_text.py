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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
print("Solution 1: zip方法")
a=text.split()
x=[]
for i in a:
    if i.isalpha() is True:
        x.append(i)
c=[]
for i in x:
    b=x.count(i)
    c.append(b)
n_dic=dict(zip(x,c))
sorted_dic=sorted(n_dic.items(),key=lambda n_dic:n_dic[1],reverse=True)
print(dict(sorted_dic))

print("Solution 2: dict方法")
a=text.split()
x=[]
for i in a:
    if i.isalpha() is True:
        x.append(i)
n_dic={}
for word in x:
    if word not in n_dic:
        n_dic[word]=1
    else:
        n_dic[word]=n_dic[word]+1
sorted_dic=sorted(n_dic.items(),key=lambda n_dic:n_dic[1],reverse=True)
print(dict(sorted_dic))
