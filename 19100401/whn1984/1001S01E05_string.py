print("将字符串样本text里的better全部替换成worse")
text = '''The Zen of Python, by Tim Peters
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
print(text.replace('better','worse'))

print("将第2步结果中包含ea的单词剔除")
my_list = text.split()
str1="ea"
str2=[]
for i in my_list:
    if i.find(str1) < 0:
        str2.append(i)
print(str2)

print("将第3步的结果里的字母进行大小写翻转")
text=text.swapcase()
print(text)

print("将所有单词按a...z升序排列")
my_list_1=text.split()
my_list_1.sort()
print(my_list_1)