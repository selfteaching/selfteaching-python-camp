'''
统计字符串样本中英文单词出现的次数
'''
text='''
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
# 将文本全部小写同时分割成单词
list_text=text.lower().split()
# 存放正常的英文单词
words=[]
#剔除特殊字符并删除空字符，使用 str 的 strip 方法
for i in range(len(list_text)):
    list_text[i]=list_text[i].strip('*--!.,\'')
    if len(list_text[i]):
            words.append(list_text[i])

# #剔除特殊字符并删除空字符,使用 str 的 replace 方法
# symbols='*--!.,‘
# for word in list_text:
#         for symbol in symbols:
#              word=word.replace(symbol,'')
#         if len(word):
#                 words.append(word)

print('不包含特殊字符的英文单词：',words)



# 使用字典类型统计文本中单词数

# 定义空字典用于存放单词及单词数
word_dic={}
# # 存放过程
# for word in words:
#     if word in word_dic.keys():
#         word_dic[word]=word_dic[word]+1  
#     else:
#         word_dic[word]=1
# print(word_dic)

# 存放过程，使用集合set
keys_set=set(words)
for word in keys_set:
        word_dic[word]=words.count(word)
print(word_dic)    

# 对字典的值降序排列，使用内置函数 sorted
# 字典的 items 方法会返回 （key,value）的元组列表
# key 使用lambda 指定按哪一项排序
list_sorted=sorted (word_dic.items(),key=lambda item:item[1],reverse=True)
# 打印统计结果  
print ('按统计次数从大到小排序：')
for i in list_sorted:
        a,b=i
        print(a,':',b)  
