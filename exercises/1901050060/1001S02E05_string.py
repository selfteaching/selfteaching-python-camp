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

#1、better替换成worse
string1 = text.replace('better','worse')

# 2、 将包含ea的单词去掉

newword = string1.split()
string2=[]
for i in newword:
    if "ea" not in i:
        string2.append(i)
string3=' '.join(string2)

# 3、大小写翻转
string4=string3.swapcase()
#4、升序排列
string5=string4.replace(","," ").replace("."," ").replace("--"," ").replace("!"," ").replace("*"," ")
newword2=string5.split()
newword3=sorted(newword2)
string5=' '.join(newword3)

print(string5)