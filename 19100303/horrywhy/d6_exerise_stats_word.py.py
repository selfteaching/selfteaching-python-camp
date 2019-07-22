string1 =  '''
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
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。
'''

import collections
import re

def stats_text_en(string_en):

    result = re.sub("[^A-Za-z]", " ", string_en.strip())
    newList = result.split( )

    for i in range(0,len(newList)):
        newList[i]=newList[i].strip('*-,.?!')
        if newList[i]==' ': 
            newList[i].remove(' ')
        else:
            i=i+1
    print('英文单词词频统计结果： ',collections.Counter(newList),'\n')


def stats_text_cn(string_cn):
    ''' 统计中文汉字字频
    
    第一步：过滤汉字字符，并定义频率统计函数 stats()。
    第二步：清除文本中的标点字符,将非标点字符组成新列表 new_list。
    第三步：遍历列表，将字符同上一次循环中频率统计结果作为形参传给统计函数stats()。
    第四步：统计函数在上一次统计结果基础上得出本次统计结果，赋值给newDict。
    第五步：new_list遍历结束，输出倒序排列的统计结果。
    '''
    result1 = re.findall(u'[\u4e00-\u9fff]+', string_cn)
    newString = ''.join(result1)

    def stats(orgString, newDict) :
        d = newDict
        for m in orgString :
            d[m] = d.get(m, 0) + 1
        return d
    
    new_list = []
    for char in newString :
        cn = char.strip('-*、。，：？！……')
        new_list.append(cn)
    
    words = dict()
    for n in range(0,len(new_list)) :
        words = stats(new_list[n],words)
    newWords = sorted(words.items(), key=lambda item: item[1], reverse=True) 
    print('中文汉字字频统计结果： ',dict(newWords))

# 调用函数
stats_text_en(string1)
stats_text_cn(string1)