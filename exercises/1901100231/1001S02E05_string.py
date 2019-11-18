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
'''#要处理的文本
text = text. replace ("better","worse")#用replace函数进行关键词的替换
text = text. replace ("\n"," ")#去除换行符，使结果更美观
text = text. replace ("*","")
text = text. replace ("--","")
text = text. replace (".","")#去除其他符号，否则会影响后续统计
copy = text.split(' ')#将字符串转化为列表，便于之后的操作
copy = [x for x in copy if x != '']#去除列表中的空格元素，否则总是有空格会参与排序
copy = [x for x in copy if "ea" not in x]#找出copy中的含“ea”的元素并删去，用循环加条件判断会有漏网之鱼，原因不明  
text = ' '.join(copy)#由于大小写转换命令只适用于字符串，故转换回字符串
text=text.swapcase()#进行大小写互换
copy = text.split(' ')#为了排序，在不更改任务顺序的前提下再次转化为列表进行排序
copy.sort()
print(copy)    

