import re  # 正则表达式
text=('''The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!''')


text2=text.replace("better","worse")  #用replace将文本中 better 全部替换成 worse
print (text2)

text3=text.split() #split将字符串转换成列表
print (text3)

text4 = []

for i in text3: #for是发起循环的关键词；i in text3是循环规则，i是依次得到txet3列表中的各个值，然后按照索引顺序循环下去，直到最后一个
    if i.find("ea") < 0: #这个if语句是判断“ea"是不是在某个单词里面
        text4.append(i)
    print (text4)

text5=text.swapcase()#用swapcase将文本中的大小写字母进行互换
print(text5)

text6=text3.sort() #先用split将字符串改成列表形式 然后再用sort进行排序  这里用text3是因为 text3是已经转变完成的列表
print(text3)








