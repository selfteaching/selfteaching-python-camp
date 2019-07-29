# coding=utf-8 

##########################################################################
##########################################################################
# 定义中文词频函数
# 设置默认的汉语参数
def stats_text_cn(text= '默认：鸡生蛋，蛋生鸡，吃鸡蛋。'):

  text = input('请输入汉字:')
  # 如果从终端没有输入任何东西，那么text采用默认数据
  if text == '' : 
    text = '默认：鸡生蛋，蛋生鸡，吃鸡蛋。'

  print('接收到的内容是：\n',text)
  import string
 
  # 将接收到的字符串转换成列表
  text_list = list(text)    #使用list()函数
  print('输出单个的汉字-列表：')
  print(text_list)    

  # 使用filter()函数，将列表中的标点符号过滤掉。
  # 可以直接赋值给原列表
  text_list = list(filter(lambda x: '\u4e00'<=x<='\u9fa5' , text_list))
  print('去掉标点符号后的汉字列表：')
  print(text_list)    
 

  # 使用set()函数，将列表转换成集合后，自动去除了列表中重复的汉字
  text_set =()
  text_set = set(text_list)
  print('无重复的汉字的数量为：')
  print(text_set)

 
  # 用字典统计单词的个数
  text_dict = {}   # 定义一个字典
  # 用字典的推导式来生态字典的元素
  # 使用count()函数，统计列表中单词的个数
  text_dict = {word:text_list.count(word) for word in text_set}

 
  # 对字典进行排序，使用sorted()函数，按频率从大到小排序（按字典的value值进行排序）
  list_new =[]
  list_new = sorted(text_dict,key=lambda x:text_dict[x],reverse=True)
  # sorted()函数只能返回这个字典的key————返回值是只有key的一个列表
  # 相要得到{单词：频数}的字典，必须利用原来的字典text_dict，创建一个新的字典
  text_newdict ={}
  text_newdict = {word:text_dict[word]  for word in list_new}
  print('按数量，从大到小输出汉字及个数：\n',text_newdict)



###################################################################################
###################################################################################
# 定义英文词频函数
# 将 the zen of python 设置为函数的默认参数。使用\连接两行句子
def stats_text_en(text= '''The Zen of   Python , by Tim Peters   \
  Beautiful is better than ugly.\
  Explicit is better than implicit. \
  Simple is better than complex. \
  Complex is better than complicated.\
  Flat is better than nested. \
  Sparse is better than dense. \
  Readability counts. \
  Special cases aren't special enough to break the rules. \
  Although practicality beats purity. Errors should never pass silently. \
  Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. \
  There should be one-- and preferably only one --obvious way to do it. \
  Although that way may not be obvious at first unless you're Dutch. \
  Now is better than never. Although never is often better than *right* now. \
  If the implementation is hard to explain, it's a bad idea. \
  If the implementation is easy to explain, it may be a good idea. \
  Namespaces are one honking great idea -- let's do more of those!'''):

  print('接收到的内容是：\n',text)
  import string
 
  # 拆分text
  text_chaifen = text.split()    #拆分字符串
  print('输出拆分字符串的结果-列表：')
  print(text_chaifen)    #对字符串使用split()方法的结果，是返回一个列表

 
  # 去掉两端空格
  text_chaifen = [word.strip()  for word in text_chaifen]
  # 去掉单词两端的空格。可以直接赋值给原列表
  print('去掉两端的空格：')
  print(text_chaifen)

 
  # 去掉单词两端的标点符号。可以直接赋值给原列表
  text_chaifen = [word.strip(string.punctuation)  for word in text_chaifen]
  print('去掉单词两端的标点符号：')
  print(text_chaifen)    # 纯粹的标点符号被strip()成“”（空）—————什么都没有nome

 
  # 应除去列表中的空“”元素，使用filter()函数
  text_notnone= list(filter(lambda x: len(x)>0  ,text_chaifen))
  # filter()函数只能返回一个迭代器对象，不能返回列表
  # 要使用list()函数，才能将迭代器对象转换成列表
  # 与之相似的是，对列表使用enumerate()函数，也只能返回一个迭代器对象
  # 或者使用tuple()函数，转换成元组后，也可以打印输出
  print('去掉单词列表中的空元素：')
  print(text_notnone)

 
  # 为避免将同一个单词的大小写识别为两个单词
  # 现在，全部转换成大写单词
  text_notnone = [wrod.upper()  for wrod in text_notnone]
  print('大写的单词-单词的总量为：',text_notnone)

 
  # 忽略重复的单词，统计单词的净量
  #使用set()函数，将列表转换成集合后，自动去除了列表中重复的元素
  text_set =()
  text_set = set(text_notnone)
  print('单词的净量为：')
  print(text_set)

 
  # 用字典统计单词的个数
  text_dict = {}   # 定义一个字典
  # 用字典的推导式来生态字典的元素
  # 使用count()函数，统计列表中单词的个数
  text_dict = {word:text_notnone.count(word) for word in text_set}

 
  # 使用sorted()函数，按频率从大到小排序（按字典的value值进行排序）
  list_new =[]
  list_new = sorted(text_dict,key=lambda x:text_dict[x],reverse=True)
  # sorted()函数只能返回这个字典的key————返回值是只有key的一个列表
  # 相要得到{单词：频数}的字典，必须利用原来的字典text_dict，创建一个新的字典
  text_newdict ={}
  text_newdict = {word:text_dict[word]  for word in list_new}
  print('从大到小输出单词及次数：\n',text_newdict)



'''
text = The Zen of   Python , by Tim Peters
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

#########################################################################################
#########################################################################################

stats_text_en()

stats_text_en('we are , ,WHAT WE Are!')

stats_text_cn()

