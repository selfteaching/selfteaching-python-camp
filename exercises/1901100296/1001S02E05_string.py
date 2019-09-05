'''
一、字符串的基本处理
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

'''
1、将文本中的所有better替换成worse
'''
text1=text.replace('better','worse')
print('1、将文本中的所有better替换成worse:',text1)

'''
2、剔除包含ea的单词
'''
# 先将文本按单词分割成列表
list_text1=text1.split()
# 方法一：将列表中包含ea的单词删除
# i=0               
# while i<len(list_text1):
#         if 'ea'in list_text1[i]:
#                 del list_text1[i]
#                 i=0
#         else:
#                 i=i+1
# list_text2=list_text1


# # 方法二：将列表中不包含ea的单词取出，使用序列的基本操作：not in
# list_text2=[]
# for word in list_text1:
#         if 'ea' not in word:
#                 list_text2.append(word)

# 方法三：将列表中不包含ea的单词取出，使用str的find方法
list_text2=[]
for word in list_text1:
        if word.find('ea')<0:
                list_text2.append(word)

# 输出结果
print('2、剔除包含ea的单词：',list_text2)

'''
3、将文本中的字母大小写翻转
'''
# # 将列表转换成字符串，使用str的swapcase函数
# text2=''.join(list_text2)
# text3=text2.swapcase()
# print('3、将文本中的字母大小写翻转:',text3)

# 利用 列表推到式 对 str 类型的数据进行大小写翻转
list_text3=[i.swapcase() for i in list_text2]
print('3、将文本中的字母大小写翻转:',list_text3)

'''
4、所有单词按a...z升序排列列
'''
# # 如果步骤3中输出结果是文本，先将文本转换成可变序列list
# list_text3=text3.split()
#去除单词前后的特殊字符
for j in range(len(list_text3)):
        list_text3[j]=list_text3[j].strip("*\'--.,!")
# print ('4、所有单词按a-z升序排列列:',list_text3.sort())
print ('4、所有单词按a-z升序排列列:',sorted(list_text3))