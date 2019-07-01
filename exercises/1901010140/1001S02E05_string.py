#将字符串串样本 text ⾥里里的 better 全部替换成 worse
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
str1=text.replace('better','worse')
print(str1)
#从第 2 步的结果里，将单词中包含ea的单词剔除(方法一)
str1_split = str1.split()
str2_1 = []
for i in str1_split:
    if "ea" not in i:
        str2_1.append(i)
print(str2_1)
#从第 2 步的结果里，将单词中包含ea的单词剔除(方法二)
t1=str1.splitlines()   
# print(ll)
#遍历列表
for s in t1:
    #按空格切割
    t2=s.split(" ")
    for s2 in t2:
        if "ea" in s2: #判断”ea"是否在第二次切割的单词中；
            str2_2=str1.replace(s2,"")  
print(str2_2)
#从第 2 步的结果里，将单词中包含ea的单词剔除(方法三)
str1_split = str1.split()
str2_3 = []
for i in str1_split:
    if i.find('ea') < 0:
        str2_3.append(i)
print(str2_3)
#将第 3 步的结果里的字⺟进行大小写翻转（将大写字母转成小写，小写字母转成大写,方法一）
str3_1=str2_2.swapcase()
print(str3_1)
#将第 3 步的结果里的字⺟进行大小写翻转（将大写字母转成小写，小写字母转成大写，方法二）
a = ''
b = a.join(str2_2)#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
#语法join()方法语法：str.join(sequence)
str3_2 = b.swapcase()
print(str3_2)
#将第 4 步的结果⾥里里所有单词按 a…z 升序排列列，并输出结果

str3_1=text.replace(',','').replace('.','').replace('*','').replace('--','').replace('!','')

t4 = str3_1.split()
str4 = sorted(t4)
print(str4)