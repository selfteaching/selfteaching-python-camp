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
#将字符转换为空格
text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')

#统一单词成小写
text=text.lower()

#拆分单词
text=text.split()

#转换字符串为字典
a={}
for i in text:  
    a.update({i:text.count(i)})#update语法用来添加，count用来计算出现次数
print(a)

#把单词按出现次数排序,key=lambda c:c[1]代表以字典第二个数据为依据排列，reverse=ture代表倒序，false代表正序
b=sorted(a.items(),key=lambda c:c[1],reverse=True) 
print(b)