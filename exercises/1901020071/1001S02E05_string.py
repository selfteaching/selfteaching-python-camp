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

#把字符串的better替换为worse
str1=text.replace("better","worse")
#print(str1)

#把str1按行切割成列表
ll=str1.splitlines()   
# print(ll)

#遍历列表
for s in ll:
    #按空格切割
    l2=s.split(" ")
    for s2 in l2:
        if "ea" in s2: #判断”ea"是否在第二次切割的单词中；
            str1=str1.replace(s2,"")  #如果ea在单词中，把单词替换为空；

print(str1)

#大写字母转换为小写，小写字母转换为大写
str2=str1.swapcase()
print(str2)

#将str2结果里所有的单词按a...z的升序进行排列，并输出结果：
str3=str2.replace("\n","").replace("."," ").replace("!","").replace("--","").replace("*","")
str4=str3.split(" ")
#print(str3)

#sorted(str4,key=str.lower)

str4.sort(key=str.lower)
print(str4)


