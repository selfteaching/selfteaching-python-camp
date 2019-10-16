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


# 将better 替换成 worse,并输出
text_re = text.replace('better','worse')
print('将better 替换成 worse:\n',text_re)   #对字符串使用replace()方法后，返回值仍然是字符串。


# 将包含ea的单词剔除，并输出
text_re_chaifen = text_re.split()    #拆分字符串
print('输出拆分字符串的结果-列表：',text_re_chaifen)    #对字符串使用split()方法的结果，是返回一个列表。

text_re_chaifen = [word.strip()  for word in text_re_chaifen]  # 去掉单词两端的空格。可以直接赋值给原数组
print('去掉两端空格：')
print(text_re_chaifen)

text_re_chaifen = [word.strip(string.punctuation)  for word in text_re_chaifen]  # 去掉单词两端的标点符号。可以直接赋值给原数组
print('去掉单词两端的标点符号：')
print(text_re_chaifen)    #纯粹的标点符号将被strip()成''(空)——什么都没有。

# 应将除去列表中的空元素，使用filter()方法
text_re_chaifen= list(filter(lambda x: len(x)>0  ,text_re_chaifen))
# filter()函数只能返回一个迭代器对象，不能返回列表
# 或者使用tuple()转换成元组，然后也可以打印输出
print('去掉单词列表中的空元素：')
print(text_re_chaifen)

# 尝试使用filter()函数过滤掉含ea单词
text_re_notea= list(filter(lambda x: ('ea' not in x)  ,text_re_chaifen))  # 使用了成员运算符 not in
# filter()函数只能返回一个迭代器对象，不能返回列表
# 或者使用tuple()转换成元组，然后也可以打印输出
print('使用filter()函数过滤掉含ea单词:')
print(text_re_notea)


# 大小写交叉转换  用到   .swapcase()方法
text_re_aswapA = [word.swapcase() for word in text_re_notea]
print('大小写交叉转换  用到   .swapcase()方法:')
print(text_re_aswapA)


# 按a-z升序排列
print('按a-z升序排列:')
print(sorted(text_re_aswapA,key= lambda word:word.lower() ,reverse=False))




