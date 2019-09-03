#Selflearning day5 homework Part1 ,handling string!

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
# 1.使用字典统计样本中各个英文单词出现的次数

t1=text.lower() #将text lower

t2=t1.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')  #将非英文字符替换为空格

t3=t2.split() #将str 转成list 

d1={} #define dict

for i in t3:
    d1.setdefault(i,t3.count(i))  #将列表中的单词及单词的出现次数，分别赋值给d1的键和值

print(d1)

# 2.按照出现次数从大到小输出所有的单词及出现的次数
d2 = sorted(d1.items(),key = lambda items:items[1],reverse = True)      #将d1按照value值从大到小排列，并将结果赋值给元祖d2
print(d2)

d3 = sorted(d1.items(),key = lambda items:items[1],reverse = False)      #将d1按照value值从小到大排列，并将结果赋值给元祖d3
print(d3)


            
