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
In the face of ambxiguity, refuse the temptation to quess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never..
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#1.better替换成worse
string1=text.replace('better','worse') #原字符串text不会改变，需要定义新的字符串string1

#2.将含有ea的单词删除
string2=string1.split() #str.split()分割字符串，默认以空格进行分割.  【未去掉标点符号】
string3="ea"
string4=[]
for i in string2:
    if i.find(string3)<0: #单词不含有‘ea’
        string4.append(i) #append()用于在【列表】末尾添加新的对象
string5=" ".join(string4) #str.join(obj)通过指定字符连接序列中元素后生成的新字符串，将列表string4转换成字符串string5。【未去掉标点符号】

#大小写翻转
string6=string5.swapcase() #str.swapcase()大小写互换

#4.a-z排序
string7= string6.replace(","," ").replace("."," ").replace("--"," ").replace("!"," ").replace("*"," ") #【去掉标点符号】
string8= string7.split()
string9= sorted(string8,key=str.lower) #sorted()排序，key：用列表元素的某个属性或函数进行作为关键字（按小写字母进行排序）
string10= " ".join(string9)
print(string10) #【输出无标点符号】
