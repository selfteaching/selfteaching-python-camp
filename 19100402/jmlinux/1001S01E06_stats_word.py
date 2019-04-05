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
text2 = '''Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，
          最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，
          越来越多被用于独立的、大型项目的开发。
'''
 
import collections 
import re

def stats_text_en(str_en):   #函数实现统计每个英文单词出现的次数，返回一个按词频降序排列的数组
    list1 = str_en.split()  #分割单词
    i=0
    for i in range(0,len(list1)):   #遍历列表
        list1[i]=list1[i].strip('*-,.!') #移除字符
        if list1[i]==' ': 
            list1[i].remove(' ')         #去掉空格
        else:
            i=i+1                        #自加1
    return collections.Counter(list1)    #统计并返回结果


def stats_text_cn(str_cn):   # 统计中文汉字字频
    str1 = re.findall(u'[\u4e00-\u9fff]+', str_cn)   #过滤汉字字符
    newString = ''.join(str1)  

    new_list = []
    for char in newString :          #清除文本中的标点字符
        cn = char.strip('-*、。，：？！……')
        new_list.append(cn)                #将非标点字符组成新列表 new_list
    return collections.Counter(new_list)   #统计并返回结果


print("统计英语字频",stats_text_en(text))  #调用并显示
print("统计中文汉字字频",stats_text_cn(text2))  #调用并显示
