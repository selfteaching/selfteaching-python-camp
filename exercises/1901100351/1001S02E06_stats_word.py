text = '''
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
import re
def stats_text_en(text):  #定义函数
    '''
    这是一个统计英文词频并按出现次数降序排列的函数
    '''
    text_1 = re.sub('\W',' ',text) #不是字符的，都转换为空格,主要去除标点符号
    text_1 = text_1.lower() #转换为小写
    textlist_1 = text_1.split() #将段落转换为列表
    dict1 = {} #定义字典
    for i in textlist_1:
        num= textlist_1.count(i)#统计词频
        r1 = {i:num}#定义元组
        dict1.update(r1)#更新词典
        dict2=sorted(dict1.items(),key = lambda dict_items:dict_items[1], reverse=True)#排序
    return(dict2)
print(stats_text_en(text))


def stats_text_cn(text_cn):#设定函数
    '''
    这是一个统计中文汉字字频并按出现次数降序排列的函数
    '''

    word_dict = {} #定义一个空字典，作为结果容器
    cn_list = list(text_cn) #将文本直接拆分为列表
    for s in cn_list: #统计中文汉字个数，并将结果返回word_dict中
        if '\u4e00'<= s <= '\u9fff':#中文字符的代码区间
            count=cn_list.count(s)#统计字符出现次数
            r1={s:count}#定义字典中的元组
            word_dict.update(r1)#更新列表
    word_sorted = sorted(word_dict.items(), key=lambda items:items[1],reverse=True) 
    #按字频降序排列输出结果
    return word_sorted

text_cn = '''
人类历史纷繁芜杂，到底什么才是最重要、最核心的推力？
是精英，还是民众？是制度，还是技术？是欲望，还是道德？
很多时候，似乎是精英主导社会，但也有许多时候，民众的力量也能摧枯拉朽；
很多时候，似乎是制度塑造社会，但也有许多时候，技术的进步会带来制度的重构；
很多时候，似乎是人们的欲望推动着社会，但也有许多时候，道德的力量也能重振河山。
'''
print(stats_text_cn(text_cn))