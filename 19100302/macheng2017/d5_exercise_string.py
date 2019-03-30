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
#  思路:
#  1.安空格将 str 拆分成数组
#  2.遍历查找数组中的better 并修改为worse
#  3.遍历数组并查找数组中的单词,包含ea的单词,并删除
#  4.遍历数组中的单词,判断是否为大写如果是大写则翻转为小写,反之亦然
#  5.对数组中的单词,安升序排序

arrText = text.split()
num = len(arrText)
otherList = []
print(num)
for i in range(num):
    if arrText[i] == 'better':
        arrText[i] = 'worse'
    if 'ea' not in arrText[i]:
        # print(i)
        otherList.append(arrText[i])
        # print(arrText[i])
    # print(arrText[i])
for j in range(len(otherList)):
    # if otherList[j].islower() == False:
    #     word = otherList[j]  
    #     word[0]
    otherList[j] = otherList[j].swapcase()

print(' '.join(sorted(otherList)))

# 总是将问题想复杂,直接找到swapcase就可以了