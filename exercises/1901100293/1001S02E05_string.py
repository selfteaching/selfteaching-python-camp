text ='''
The Zen of Python, by Tim Peters.
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
#复杂的方法
a=text.split()  #先转化类型，把str转化为list
b=a.count('better') #计算‘better’的数量赋值给b
while b!=0: #直到b不等于0，即没有单词‘better’停止
    c=a.index('better') #找到第一个‘better’的位置索引
    a.insert(c,'worse') #把‘worse’插到对应位置
    a.remove('better') #删掉第一个‘better’ 
    b=a.count('better') #再次计算‘better’剩余数量给while进行循环
#操作结束，结果是a，下方都是为了打印，此时a是list————————————————————————————
a=" ".join(a) #重新把list转化为str
p=a.replace('. ','.\n') #整理格式，找到句号位置加上换行符
print('一个个单词进行替换\n'+p) #打印出结果，这里中文说明和p都是str类型，中间可以用+号，用逗号则需要强调sep为空，否则会出现空格


#直接替换
a=text.replace('better','worse') #直接用str的命令replace替换
#操作结束，结果是a，下方都是为了打印，此时a是str————————————————————————————
print ('直接替换\n'+a)


#替换ea
a=a.split() #转化list
d=[]    #定义d为空
for b in a: #遍历a并赋予b
    if b.find('ea')<0: #b是a的遍历，b是str型，可以用find进行查找，小于零则说明当前b不包含‘ea’
        d.append(b) #将不包含ea的b加入到d中，d是list类型
#操作结束，结果是d，下方都是为了打印，此时d是list————————————————————————————
print('替换完成的list\n',d,sep='') #这里d是list，中文说明是str，不能用+号
p=" ".join(d)   #转化类型为str
p=p.replace('. ','.\n') #整理格式，找到句号位置加上换行符
print('整理好的文案\n',p,sep='') #这里p前面是逗号，则需要强调sep为空，否则p的前面会有一个空格


#反转大小写
d=" ".join(d)   #转化类型为str
d=d.swapcase()  #使用str的swapcase进行反转大小写
#操作结束，结果是d，下方都是为了打印，此时d是str————————————————————————————
p=d.replace('. ','.\n') #整理格式，找到句号位置加上换行符
print('反转大小写\n',p,sep='') #这里p前面是逗号，则需要强调sep为空，否则p的前面会有一个空格


#排序
d=d.split() #转换类型
d.sort()    #对d进行排序
print('排序\n',d,sep='')    #打印输出