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
Namespaces are one honking great idea -- let's do more of those! '''
text1 = text.lower()
alphaList="abcdefghijklmnopqrstuvwxyz "
text2 =''
for i in text1:
        if i in alphaList:
                text2 = text2+i #去除多余非字母字符
list1 =text2.split() #存储text单词化的列表
list2 = list(set(list1))#单词不重复的列表
list2.sort()
j=0
dictData = {}
for word in list2:
        j = list1.count(word)
        dictData[word] = j #生成字典类型

#print(dictData)
listTemp = list(set(list(dictData.values())))
listTemp.sort(reverse = True) #从小到大排列value
#按单词出现的次数从大到小打印输出
dictFinal = {}
for i in listTemp:
        for key in dictData:
                if dictData[key] == i:
                        dictFinal[key] = i
for item in dictFinal.items():
        print(item)


