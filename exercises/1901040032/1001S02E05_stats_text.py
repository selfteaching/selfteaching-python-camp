text="""
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
# 下面的代码是在统计text中个单词出现的次数

d={}
print("清除所有非英文字符")
for x in text.split():   # 将text中的文本以空格切分为一个数组，遍历这个数组
    y = x.strip(' -,.*!') # 装数组中的元素去除掉特殊字符
    print(y)

    if y not in d:   # 如果字典d中不存在这个元素，则将这个元素作为key，存放在这个数组里面，value初始化为1
        d[y] = 1
    else: # 如果字典d中存在这个元素，则将这个元素对应出现的次数（value）取出来加上一次再放回去
        d[y] = d[y] + 1 
print("每个单词出现的次数")
print(d)