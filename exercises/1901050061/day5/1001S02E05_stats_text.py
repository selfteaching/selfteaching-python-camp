t = '''
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

# 使用“字典”统计以上文本中出现的单词次数
# 按照上一步的结果从大到小输出

t = t.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ') # 去标点，连续操作很棒
print(t)
t = t.lower() # 全部换成小写
print(t)
t = t.split() # 拆成列表
print(t)
d = {} # 上字典
for i in t:
    count = t.count(i) # 数数
    r1 = {i:count} # 单词在前，词频在后
    d.update(r1) #上传r1到d中去
print(d)

#print('\n按照出现次数多少输出所有单词\n')，不理解
d = sorted(d.items(),key=lambda x:x[1],reverse=True)
# sorted(iterable,*,key=None,reverse=False) lambda是个特殊的定义函数，后面是的定义的表现形式，留待以后研究，reverse=True是颠倒的意思
print(d)