#Step1
text='''
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
'''

#Step2:将字符串串样本text⾥里里的better全部替换成worse
text1 = text.replace('better','worse')
print(text1)

#Step3:从第 2 步的结果⾥里里，将单词中包含 ea 的单词剔除
text2=text1.split()
print(text2)

text3=[]
for i in text2:
    if'ea' not in i:
        text3.append(i)
print(text3)

#Step4:将第3步的结果里的字母进⾏⼤⼩写翻转(将大写字母转成小写，⼩写字母转成大写)
text4=(" ".join(text3))
text5=text4.swapcase()
print(text5)

#将第4步的结果⾥所有单词按a...z升序排列，并输出结果
list = text5.split()
print(r'',sorted(text5.split())) 