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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
listwhole = text.split()  #获得完整单词列表
listok = list(set(listwhole))  #去重单词列表,set集合为无序不重复列表


#使用字典(dict)统计字符串样本text中各个英⽂单词出现的次数:
dic = {} #创建空字典,使处理后字典中的键为单词，值为次数。
for i in range(len(listok)):#利用for循环为单词重复次数计数
    dic[listok[i]] = 0   #字典初始值设置为0,listok[i]是单词，做为dic的key。
    for j in range(len(listwhole)):
        if listok[i] == listwhole[j]:#listok是不重复单词列表，listwhole是有重复单词列表
            dic[listok[i]] += 1
print('\n单词计数字典dic为:\n{}'.format(dic))


#按照出现次数从⼤到⼩输出所有的单词及出现的次数
l = list(dic.items())  #字典变成元素为元组的列表,后面应用列表排序，再变回字典，遍历打印字典key和value
def invert(lis):   #定义翻转列表函数，目的是：由字典items变成列表后，其元素为包含两个元素的元组，把这两个元素互换。
	for i in range(len(lis)):
		a,b = lis[i]  #此函数要求lis[i]元组仅2个元素
		lis[i]=(b,a)
	return lis

newl = invert(l.copy())   #翻转列表元素，使数字在前，便于排序
newl.sort(reverse = True)  #从大到小排序新列表
l2 = invert(newl.copy())  #将排序的列表再翻转其中的元组的两元素
aimdic = dict(l2)  #改好次序的目标字典
print(aimdic)
print ('\n按照出现次数从大到小输出所有的单词及出现的次数：')
for i in aimdic.items():  #利用for循环遍历其中key和value
	a,b = i[0],i[1]
	print(a,':',b)  #按照出现次数从⼤到⼩输出所有的单词及出现的次数


#只统计英文单词，不包括非英文字符的其它任何符号，如连接符号，空白字符等
#从text中就删去特殊字符，再重复上述操作。
text1 = ''
for i in range(len(text)):   #利用for循环遍历text来删除特殊字符
    if text[i] != '*' and text[i] != '-':
        text1 +=text[i]   #得到符合无特殊符号的新字符串text1
listall = text1.split()   #字符串变列表
listnorep = list(set(listall))   #去重单词列表
dic1 = {}   #创建空字典用来统计单词出现次数
for i in range(len(listnorep)):   #遍历不重复单词列表listnorep
    dic1[listnorep[i]] = 0   #字典初始值设置为0
    for j in range(len(listall)):   #遍历全部单词列表listall
        if listnorep[i] == listall[j]:
            dic1[listnorep[i]]  +=  1   #重复一次加一次，得到单词计数字典。
l1 = list(dic1.items())    #字典变成元素为元组的列表,后面应用列表排序，再变回字典，遍历打印字典key和value
nl1 = invert(l1.copy())
nl1.sort(reverse = True)
nl2 = invert(nl1)   #排序后还有翻转，因为字典key值不可以有相同的
aim = dict(nl1)
print ('\n按照出现次数从大到小输出所有的不含特殊符号的单词及出现的次数：\n')
for i in list(aim.items()):  #利用for循环遍历字典items
	a,b = i[0],i[1]   #
	print(b,':',a)  #按照出现次数从⼤到⼩输出所有的单词及出现的次数
