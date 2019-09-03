text= '''
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

# 任务1 用 worse 替换 better (replace 的语法格式是 用后面的替换前面的)
a=text
b=a.replace('better','worse')
print(b)
#任务2 将上一步结果中将包含ea的单词剔除
c=b.split() #先把上面的字符分开，用 split()通过指定分隔符对字符串进行切片
d='ea'       #这样找出含ea的单词
e=[]         #方括号是生成一个列表
for i in c:
    if i.find(d)<0:  #Python find() 方法检测字符串中是否包含子字符串 ,
                      #如果包含子字符串返回开始的索引值，否则返回-1, 这时<0还没弄清什么意思
        e.append(i)    #重新生成e 这个列表，且是后面附加了i 这个条件的列表
print(e)               
#任务3 上一步结果大小写转换。
f=a.swapcase() #这个简单 swapcase() 方法用于对字符串的大小写字母进行转换 swap就是互换的意思。
print(f)
#任务4 将上步操作后的结果所有单词按A-Z顺序排列，并输出结果。
g=e.sort()   #对列表中的元素进行排序, 这时是把e sort  一下
print(g)
