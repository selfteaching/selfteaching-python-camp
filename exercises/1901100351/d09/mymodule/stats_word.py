# this is d9 exercise for stander libirary
# date: 2019.09.20
# author by: rtgong

# 统计参数中英文单词出现的次数，并按降序排列
def stats_text_en(text):  #定义函数
    import collections
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型,输入类型 %s' % type(text))
    text = text.replace(',','').replace('.','').replace('!','').replace('--','').replace('*','').replace('(','').replace(')','')
    list_text = text.split()
    count = int(input("请输入要限制输出的元素个数："))
    dic = collections.counter(list_text).most_common(count)
    return dic

# 统计参数中汉字出现次数，并按降序排列
def stats_text_cn(text):#设定函数
    dic = {}
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型,输入类型 %s' % type(text))
    
    for i in text:
        if '\u4e00'<= i <= '\u9fff':#中文字符的代码区间
            dic[i] = text.count(i)
    import collections
    count = int(input("请输入要限制输出的元素个数："))
    dic = collections.Counter(dic).most_common(count)
    return dic
    

# 合并英汉词频统计
def stats_text(text) :
    dic_1 = stats_text_cn(text)
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型,输入类型 %s' % type(text))
    for i in text:
        if '\u4e00'<= i <= '\u9fff':
            text = text.replace(i,'')
    text = text.replace('「','').replace('」','').replace('，','').replace('。','').replace('？','').replace('！','').replace('：','')
    dic_2 = stats_text_cn(text)
    dic_3 = {}
    dic_3.update(dic_2)
    dic_3.update(dic_1)
    dic_3 = sorted(dic_3.items(),key=lambda x:x[1], reverse = True)

    return(dic_3)

print(stats_text.__doc__)
     

en_text = '''
the Zen of Python, by Tim Peters

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

cn_text = '''
Python之禅 by Tim Peters
 
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
尽管实用会打破纯粹，也不可违背规则 
不要包容任何错误，除非你确定需要这样做 
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是 Python 之父 
做也许好过不做，但不假思索就动手还不如不做 
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然 
命名空间是一种绝妙的理念，请多加利用
'''
