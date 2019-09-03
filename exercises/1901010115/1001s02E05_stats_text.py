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

text1 = text.lower() #文本转小写
text_list1 = text1.split() #文本转列表
dict1 = {} #定义一个空字典
for i in text_list1: #指定i历遍列表里的元素
    ii = i.strip(' ,.*!-') #清洗i收集的元素，赋值于ii
    if ii not in dict1: #依次，如果ii里的元素没在空字典里
        dict1[ii] = 1 #则增加该元素为一个新健
    else: #如果ii的的元素已经在字典里
        dict1[ii] = dict1[ii] + 1 #则该元素对应的健累加一个值
print(dict1)
print('\n')

dict2 = sorted(dict1.items(),key = lambda x:x[1],reverse = True) #items()函数意为把字典转为元组；key=lambda x:x[1]意为指定任意键(?)，以键后的数字为排列原则；True指示降序排序。
print(dict2)
