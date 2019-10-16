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
'''
m1=text.replace('better','worse')
print(m1)
#任务2 从上一步的结果里，将单词中包含ea的单词剔除
m2=m1.replace('ea', '')
print(m2)
#任务3 将上一步结果里的字母进行大小写翻转
m3=m2.swapcase()
print(m3)
#任务4 将上一步结果里所有单词按a……z升序排列，并输出结果
s1=m3.replace(".",'')  #删除.
s2=s1.replace('--','') #删除--
s3=s2.replace('*','')  #删除*
s4=s3.lower()          #转换为小写
s5=s4.split()          #拆分为列表
s5.sort()              #排序
print(s5)
    

