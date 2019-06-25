#任务1 使用字典统计字符串样本text中各个英文单词出现的次数。
s = '''The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!'''
s1 = s.replace(',','').replace('*','').replace('--','').replace('.','').replace('!','')
s2 = s1.lower() #转化小写
s3 = s2.split() #以单词为单位拆分为字符串
count={}  #建立空字典
for w in s3:
    count.setdefault(w,0)
    count[w]+=1
print(count)

#任务2 按照出现次数从大到小输出所有单词及出现的次数
items=count.items() #以列表返回可遍历的（键，值）元组
backitems=[[v[1],v[0]] for v in items] #☎调换原有的（键、值）位置变为（值、键）
l = sorted(backitems,reverse=True)#按照值倒序排列
print(l)