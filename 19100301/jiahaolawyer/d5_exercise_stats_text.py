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
def artReadToList(fn):
    with open(fn,'r')as f:
        content=f.read()
        return content.split()
str=artReadToList('d5_exercise_stats_text.py')
d=dict() #创建字典数据对象
for s in str:
    d[s]=d.get(s,0)+1  #字典 get(key,defaultvalue)方法获取key的值，默认值为0

print(d)

 
 
  
  

 
 


 

 