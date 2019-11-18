# DAY5 掌握基本数据类型 2019-11-03
#Task2：统计字符串串样本中英⽂文单词出现的次数

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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

aa = text.replace(","," ").replace("."," ").replace("--"," ").replace("!"," ").replace("*"," ").replace("\n","")
new = aa.split(" ") #分割字符串，变为列表,以空格进行分割。


print("统计单词出现次数：")
d ={} #这里要用大括号
for i in new :          
    j= new.count(i)     # 一个元素出现的: 次数 ,此处的i 就表示一个单词,上面已经分割好;另外用法 也可以是一个字符串中的 某一个或者几个字母,比如 'ea'
    d[i] = j # 这里就是把这个单词 和 出现的次数 添加到 字典中,当然也可以用 update 函数 
    #   d={i:j} #这里要用大括号
d.pop("")
print(d)


print("按出现频次数从大到小输出：")  

d1=sorted(d.items(),key=lambda x:x[1],reverse=True)   
print(d1) 
