text = '''
The zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
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
#任务1：将字符串串样本 text ⾥里里的 better 全部替换成 worse
tex1 = text.replace("better","worse") #replace是有返回值的
print(text1)
#任务2：从第 2 步的结果里，将单词中包含 ea 的单词剔除
text2 = tex1.split()  #需要将str变成list来进行操作
a = "ea"
text3 = []
for i in text2:
    if i.find(a) < 0:
        text3.append(i)
print(text3)
#任务3：大小写切换
text4 = " ".join(text3)  #大小写切换需要将list切换成str格式
text5 = text4.swapcase()
print(text5)
#任务4升序排列
text6 = text5.split()   #排序的时候需要将str再转换成list格式
text7 = text6.sort()   #排序函数没有返回值
print(text6)


        
        
