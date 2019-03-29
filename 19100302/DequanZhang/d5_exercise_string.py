 
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

#将字符串样本text中的better全部替换为worse
text1 = text.replace("better", "worse")    #字符串，一定不能忘记引号
print(text1)

#从上一步结果里，将单词中包含ea的单词剔除

a = text1.split()     #在这个地方卡了很久
for x in a:
    if "ea" in x: 
        a.remove(x)
print(a)


#将上一步结果里的字母，进行大小写翻转（将大写转为小写，小写转为大写）
print(text1.swapcase())   #最开始的时候，忘记print，所以terminal里没有实现


#将上一步结果的所有单词按a...z升序排列，并输出结果
print(sorted(a, key=str.lower))

