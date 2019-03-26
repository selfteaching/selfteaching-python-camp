import re
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

#1.把英文单词含有ea的单词剔除掉
#2.把better 替换成 worse
#3.大写字母转换成小写,小写的转换成大写
#4.将所有单词 按A-Z排列

#思路:把text文本内容转换成list的一个个元素,然后遍历处理
def remove_ea(a):
    allWords =a.split(" ")
    for item in allWords:
        if "ea" in item:
            allWords.remove(item)
    print(allWords)

#把better 替换成 worse 

def replace_worse_to_better(a):
    wordLi=a.split(" ")
    for index in range(len(wordLi)):
        if wordLi[index]=="better":
            wordLi[index]="worse"
    print(wordLi)

replace_worse_to_better(text)

#把大写转成小写,小写改为大写
def reverse_the_case(a):
    wordLi=a.split(" ")
    for index in range(len(wordLi)):
        wordLi[index]=str(wordLi[index]).swapcase()
    print(wordLi)

reverse_the_case(text)

def sort_word(a):
    wordLi=a.split(" ")
    wordLi.sort()
    print(wordLi)
sort_word(text)

