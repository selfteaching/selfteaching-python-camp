#这是一个关于字符串基本处理的程序

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

#1.1：将text中含有“ea”的单词剔除
import re
list1 = re.split(r"(\W+)",text)   #将text字符串（string）转换为列表（list）,每一个单词和其他字符（空格，换行，‘.’，‘,’，‘*’），都成为list1列表中的一个元素
for i in list1:   #当i属于list1列表当中的元素时，开始循环
    if 'ea' in i:   #判断当‘ea’属于i时，执行语句
        list1.remove(i)   #移除i

#1.2：将list1中全部的‘better’转换为‘worse’
s0 = ''
s1 = ''
s2 = ''
s1 = s0.join(list1)   #将列表list1合并为字符串s1
s2 = s1.replace('better','worse')   #将s1中全部的‘better’替换为‘worse’

#1.3：将s2中所有单词的大写字母转成小写，小写字母转成大写
s3 = ''
s3 = s2.swapcase()   #调用str类的swapcase方法，同时实现大写转小写，小写转大写的功能

#1.4：将s3中所有的单词按首字母从a到z排列，并输出结果
list2 = re.split(r"\W+",s3)   #将字符串s3转换为列表list2,只保留单词为list2中的元素
list2.sort()    #将list2中的单词按首字母从a到z排列
while '' in list2:   #删除list2中为空的列表元素
    list2.remove('')

print("最终结果为:")    
print(list2)    #输出结果