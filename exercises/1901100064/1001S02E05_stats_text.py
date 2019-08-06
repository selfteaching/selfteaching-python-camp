import string


text = '''The Zen of   Python , by Tim Peters
Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated.   
  Flat is better than nested. 
Sparse is better than dense. 
  Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. Errors should never pass silently. 
Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!

'''
print(text)


# 拆分text
text_chaifen = text.split()    #拆分字符串
print('输出拆分字符串的结果-列表：')
print(text_chaifen)    #对字符串使用split()方法的结果，是返回一个列表。


# 去掉两端空格
text_chaifen = [word.strip()  for word in text_chaifen]
# 去掉单词两端的空格。可以直接赋值给表表
print('去掉两端空格：')
print(text_chaifen)


# 去掉单词两端的标点符号。可以直接赋值给原数组
text_chaifen = [word.strip(string.punctuation)  for word in text_chaifen]
print('去掉单词两端的标点符号：')
print(text_chaifen)    # 纯粹的标点符号将被strip()成''(空)——什么都没有。


# 应将除去列表中的空元素，使用filter()方法
text_notnone= list(filter(lambda x: len(x)>0  ,text_chaifen))
# filter()函数只能返回一个迭代器对象，不能返回列表
# 或者使用tuple()转换成元组，然后也可以打印输出
print('去掉单词列表中的空元素：')
print(text_notnone)


# 为避免将同一个单词的大小写识别为两个单词
# 现在，全部转换成大写单词
text_notnone = [wrod.upper()  for wrod in text_notnone]
print('大写的单词-单词的总量为：',text_notnone)


# 忽略重复的单词，统计单词的净量。使用set()函数
text_set = set(text_notnone)
print('单词的净量为：')
print(text_set)


# 用字典统计单词的个数
text_dict = {}   # 定义一个字典
# 使用字典的推导式来生成字典的元素
text_dict = {word:text_notnone.count(word) for word in text_set}


# 使用sorded()函数，按频率从大到小排序
list_new = sorted(text_dict,key=lambda x:text_dict[x],reverse=True)
# sorted()函数只能返回这个字典的key——返回值是只有key的列表
# 想要得到{单词：频数}的字典，必须利用原来的字典text_dict重新生成字典
text_newdict = {word:text_dict[word]  for word in list_new}
print('从大到小输出单词及次数：\n',text_newdict)



