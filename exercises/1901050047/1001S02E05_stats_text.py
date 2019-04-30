# 1.使用字典(dict)统计字符串样本text中各个英文单词出现的次数
# 2.示例：{'is':10,'better':9,...}
# 3.按照出现次数从大到小输出所有的单词及出现的次数
# 4.只统计英文单词，不包括非英文字符的其他任何符号，如连接符号、空白字符等

 
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

t = text.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ')   
# 将非英文字符替换为空格

t = t.lower()   # 把大写转换为小写
t = t.split()    # 以空格，把字符串内单词拆分为列表

d1 = {}  # 定义字典

for i in t :    # 循环遍历列表中的单词
    d1.setdefault(i,t.count(i))  #   返回列表中单词出现的次数
print(d1)

d2 = sorted(d1.items(),key=lambda x:x[1], reverse=True)
# 按照出现次数从大到小输出所有的单词及出现的次数
# key=lambda 元素: 元素[字段索引] ，此处 ，对第二个字段进行排序

print(d2)   #   输出最终结果
