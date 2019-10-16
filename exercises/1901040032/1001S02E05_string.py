text = """
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
"""
text1=text.replace("better","worse")                                   #将字符串串样本text里的better全部替换成worse
print("将字符串样本text⾥的better全部替换成worse")
print(text1)

text2=text1.split()                                                 #把字符串分切成若干个无素列表
print(text2)

text3=[]
for i in text2:                                                       
    if'ea' not in i:                                                   #将单词中包含 ea 的单词剔除
        text3.append(i)           
print("将单词中包含 ea 的单词剔除")                                         
print(text3)

text4=(" ".join(text3))        
text5=text4.swapcase()                                                 #字⺟进⾏⼤小写翻转
print("将字⺟进行⼤小写翻转")
print(text5)

text6=text5.split()
print("将所有单词按a...z升序排列列")
print(sorted(text6, key=str.lower))                                    #所有单词按a...z升序排列