text = '''
the Zen of Python, by Tim Peters

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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

t1=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ').replace('!',' ')
# 去掉文本中的中文字符、英文字符、字号、连接符
text=text.split() #以空格为分隔符，将text中的字符串转换为列表

# 统计各个单词出现的次数
textDict={}#创建名称为textDict的字典
for word in text:#在text中循环查找word
    wordCount=text.count(word)#在text中查找word的次数定义为wordCount
    wordDict={word:wordCount}#创建wordCount字典,并定义word与word出现次数为一一对应的（键，值）
    textDict.update(wordDict)#将wordDict字典的“键值”更新到textDict字典中

# 按照出现次数从大到小排序
sortT1=sorted(textDict.items(),key=lambda x:x[1],reverse=True)
# sorted()表示排序，items()表示以列表返回可遍历的(键, 值) 元组数组
# 因为字典中基本元素是（键，值），即一个元组，所以要用key=lambda排序
# lambda是固定写法的隐函数，x:x[1]表示以元组中的第2个元素为对象，reverse=True表示按降序排列
print(sortT1) 