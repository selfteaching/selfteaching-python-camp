text = '''

The Zen of Python, by Tim Peters

The zen of Python, by Tim Peters



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
#任务1：将字符串串样本 text里的 better全部替换成 worse
text1 = text.replace("better","worse") #replace是有返回值的
print(text1)  #任务2：从第 2 步的结果里，将单词中包含 ea 的单词剔除
text2 = text1.split()  #需要将str变成list来进行操作
a = "ea"
for i in text2:
    if i.find(a) != -1:
        b = text2.index(i)
        del text2[b]
        continue
print(text2)
#任务3：大小写切换
text3 = " ".join(text2)  #大小写切换需要将list切换成str格式

text4 = text3.swapcase() 
print(text4)
#任务4升序排列
text5 = text4.split()   #排序的时候需要将str再转换成list格式
print(sorted(text5))    #排序函数sort和sorted的区别在于sort是应用在list上的函数，而sorted可以对任何可迭代的对象进行操作；比如list.sort() or sorted(iterable)


text4 = text3.swapcase()
print(text4)
#任务4升序排列
text5 = text4.split()   #排序的时候需要将str再转换成list格式
text6 = text5.sort()   #排序函数没有返回值
print(text5)



        
        
