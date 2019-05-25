import operator
import re
import collections



# 这里需要修改，添加参数count
def stats_text_en(text,count):
    #函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'%type(text))
    
    word_str = text.replace(','," ").replace('.'," ").replace('!'," ").replace('*'," ").replace('--'," ")
    # 2.按照空格将所有的单词分割开

    word_str = re.sub(r'[^A-Za-z]',' ',word_str)
    word_list = word_str.split()

    # 函数使用return，print的话直接打印，不方便，return可以在调用的时候使用变量进行接收
    return collections.Counter(word_list).most_common(count)


#(1)定义一个名为 stats_text_cn 的函数
def stats_text_cn(text,count):
    #(2)函数接受一个字符串 text 作为参数。如果不是字符串，则提示
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'%type(text))
    # 此处作为作业，你查一下正则中\w的含义
    word_str = re.findall(r'[\w]',text)
    str_d = ''.join(word_str)
    # 2.将上文中的字符串，用正则运算剔除所有英文字母单词，数字
    d = re.sub("[A-Za-z0-9]", "", str_d)
    # 这里只是传入一个可迭代的对象，并不是说调用之类的，不能写括号
    return collections.Counter(d).most_common(count)

def stats_text(text,count):
    if isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s' % type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)
