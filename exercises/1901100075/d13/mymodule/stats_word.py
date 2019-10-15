from collections import Counter
import jieba
#1. 封装统计英⽂单词词频的函数
def stats_text_en(text,count):    
    elements=text.split()
    b=[]
    a=',.*!-'
    for element in elements:
        for aa in a:
            element=element.replace(aa,'')
        if len(element) and element.isascii():
            b.append(element)
    return Counter(b).most_common(count)

#统计中⽂汉字字频的函数
def stats_text_cn(text,count):
    seg_list = jieba.cut(text)  # 默认是精确模式
    d=[]
    for character in seg_list:
        if len(character)>=2:
            d.append(character)   
    return Counter(d).most_common(count)
    


text= '''
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
text='''
忽然，很想醉，是因为早已心碎；
忽然，很想睡，是因为心里早已疲惫，
忽然，很想喝一杯咖啡，是因为要映衬内心的苦味；
忽然，很想一个人颓废，是因为再没有什么人让我不累!
我把你嵌在一滴泪里.幻想千年后的琥珀,我不敢低头,怕那滴泪坠下,碎了你,碎了我.碎了千年的梦,若有来生必踏遍千山万水寻找你
我像一朵孤云
'''    


def stats_text(text,count):
    '''合并英中文词频统计结果'''
    if not isinstance(text,str):
        raise ValueError('输入类型必须是字符串类型，输入类型%s'%type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)


    