from collections import Counter   
 #collections 是python内建的集合模块，Counter 是其中的一个函数,需要用到from...import...  否则counter函数出现Undefined的情况     
text = '''
The Zen of python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent't special enough to break the rules.
Although practicality beats purity.
错误 should never pass silently.
Unless explicitly silenced
In the face of ambxiguity,refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch
If the implementation is hard to explain,it's a bad idea
If the implementation is easy to explain,it's may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''
count =100
def stats_text_en (text, count):  #定义：函数+括弧；限制输出元素个数
    if not isinstance(text,(str)):   #参数检查
        raise ValueError('bad operand type')   #抛出错误

    replace_text = text.replace(',',' ').replace('.',' ').replace('--','').replace('!','').replace('*',' ').replace('\n','')  #第一步：去掉标点符号
    lower_text = replace_text.lower()          #单词全改为小写/大写
    split_text = lower_text.split()            #文本字符串拆分为用空格隔开的列表

    c = Counter()               #Counter函数统计词频
    for word1 in split_text:                       
        c[word1] += 1            

    c.most_common()             #括号内为输入数字，默认输出全部的单词词频
    return c

print(stats_text_en (text, count))


def stats_text_cn(text,count):
    if not isinstance(text,(str)):
        raise ValueError('bad operand type')


    text1 = text.replace('，' , ' ').replace('。' , ' ').replace('：' , ' ').replace('！' , ' ').replace('\n', ' ').replace('？', ' ')
    text2 = list(text1)             #汉字词频统计不需要空格符隔开

    cnt = Counter()
    for word2 in text2:
        if '\u4e00' <= word2 <= '\u9fff': #找中文字符
                cnt[word2] += 1

    return cnt

print(stats_text_cn (text,count))


def stats_text(text,count):
    '''合并统计英文词频和中文词频'''
    if not isinstance(text,str):
        raise ValueError('bad operand type')


    print(stats_text_en (text,count)+stats_text_en (text,count))
