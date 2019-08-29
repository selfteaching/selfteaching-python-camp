txt = '''
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
'''

#1.先分割字符串；2一会要处理单词，处理过的单词要放在一个list里，3样本中有各种符号要剔除，4如果是正常的单词，就放进list中
txt1=txt.split()#分割了字符
list=[]
a=',.!*'#把这些符号定义给一个变量（其实这个世界上的一切都是变量，你想使用它们第一步都是要把常量定义给它们）
#让计算机在这一串字符中遍历一次，寻找符号，把不是符号的存在list列表里面（所谓剔除，就是查找一遍要剔除的东西，把要留下的存储起来）
for i in txt1:#让i遍历一遍txt1
    for l in a:#让l里边一遍a的各种符号
        i=i.replace(l,'')#i用方法重生了，这个方法是把l中所有的符号都替换成''
    if len(i):#此时的i是删除了符号的，如果这个时候长度不为0，说明是单词了
        list.append(i)#把i里面的常量添加到list中
print(list)
        
#初始化一个字典，其实在统计字数的时候是用遍历的方式，用列表的count方法来做的
w={}
listset=set(list)
for p in listset:
    w[p]=list.count(p)
print(w)

