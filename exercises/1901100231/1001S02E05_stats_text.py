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
'''#待处理文本
text=text.lower()
#统一为小写
text=text.replace("\n"," ")#换行符不能直接替换为无，否则行末单词会和行首单词相连，影响后续统计
text=text.replace("!","")    
text=text.replace(".","")  
text=text.replace(",","")
text=text.replace("--","")
text=text.replace("*","")  
    #去除换行符和其他符号
copy = text.split(' ')#老规矩，先转换为列表，再进行统计
copy = [x for x in copy if x !=""]#去除空格，否则后续排序时会出现不明空格元素
a={}#创建空字典
for x in copy:
    if x in a:
        a[x]=a[x]+1
    else:
        a[x]=1       
for x in sorted(a,key=a.__getitem__,reverse=True):#反向排序
    print(x,a[x])

    




