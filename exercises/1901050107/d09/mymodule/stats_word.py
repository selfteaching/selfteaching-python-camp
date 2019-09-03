#<<<<<<< master
# -*- coding: utf-8 -*-
#=======

#>>>>>>> master
text ='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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


# 分别调⽤用stats_text_en , stats_text_cn ，输出合并词频统计结果
# 统计参数中每个英⽂文单词出现的次数，最后返回⼀个按词频降序排列列的数组
from functools import reduce
from collections import Counter

def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError("text is not a string")
    # 将单词分离出来
    result = text.split()
    word_list = []
    symple_set = ",.-!?"
    cnt = Counter()
    for item in result:
        # 排除单词中的特殊字符
        for symple in symple_set:
            item = item.replace(symple,'') 
        #如果在字典里，频次+1，否则写进字典
        word_list.append(item)
    return(Counter(word_list).most_common(count))
    # 排序        
    # return sorted(word_dict.items(),key = lambda x:x[1],reverse = True)
  


text2 = '''
#<<<<<<< master
1.c
#=======
1. 在 1001S02E06_stats_word.py 中定义⼀一个名为 stats_text_cn 的函数，函数接受⼀一 个字符串串 text 作为参数
2. 实现该函数的功能:统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的 数组
3. 为 stats_text_cn 添加注释说明
#>>>>>>> master
'''

# 函数接受⼀一 个字符串串 text 作为参数, 统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列的数组
def stats_text_cn(text,count):
    if not isinstance(text,str):
        raise ValueError("text is not a string")
    # 汉字都是单字符的，所以遍历就可以了
    chars = []
    cnt = Counter()
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            chars.append(char)
            print(char)    
          
    return Counter(chars).most_common(count)

# 如果输⼊入参数不不为字符串串类型则抛出 ValueError 错误，并包含完整的错误提示信息
def stats_text(): 
    if not isinstance(text,str):
        raise ValueError("text is not a string")    
    print(stats_text_en(text,5),stats_text_cn(text2,3))

# stats_text()