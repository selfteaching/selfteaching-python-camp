import collections

import jieba

def stats_text_cn(checkcn):    # 定义检索中文字符
    try:
        if not isinstance(checkcn,str):
            raise ValueError(checkcn)
    except ValueError as err:
        print('调用stats_text_cn函数，参数类型错误',type(err))
    else:
        countcn={}    # 初始化一个词典
        """Count the chinese in the text"""    # 注释
        cn_str=''    # 新建空白字符串
        count = 20   # 限制输出元素个数

        for i in checkcn:
            if u'\u4e00' <= i <= u'\u9fff':    # 中文字符的正则表达式
                cn_str = cn_str+i
        
        cn_list=jieba.cut(cn_str,cut_all=False)    # 精确模式分词

        string = '/'.join(cn_list)
        string = string.split('/')

        for i in string:
            if len(i) >= 2:    # 统计长度大于等于2的词
                countcn[i]=string.count(i)

    #   countcn = sorted(countcn.items(), key=lambda item:item[1], reverse=True)
        countcn = collections.Counter(countcn).most_common(count)
    #   c = Counter()
    #   for cn in countcn:
    #       c[cn] = c[cn] + 1

        print(countcn)
        return countcn
    finally:
        print('executing finally stats_text_cn!')

def stats_text_en(checken):    # 定义检索英文字符（在D5的作业基础上添加检查英文字符功能）
    try:
        if not isinstance(checken,str):
            raise ValueError(checken)
    except ValueError as err:
        print('调用stats_text_en函数，参数类型错误',type(err))
    else:
        counten={}    # 新字典
        entext=" "    # 空的字符串
        count = 20

        checken=checken.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    
        for i in checken:
            if i.isascii():    # 去掉非英文字符
                entext=entext+i    #放进空字符串中
            
        entext=entext.split()    # 分隔
    
        for i in entext:
            counten[i]=entext.count(i)    # 检索出来的内容放进新字典
    #   counten=sorted(counten.items(),key=lambda item:item[1],reverse=True)    # 按值排序
        counten = collections.Counter(counten).most_common(count)
    #    e = Counter()
    #    for en in counten:
    #        e[en] = e[en] + 1

        print(counten)
        return counten
    finally:
        print('executing finally stats_text_en!')


def stats_text(check):   # 定义函数
    try:
        if not isinstance(check,str):
            raise ValueError(check)
    except ValueError as err:
        print('调用stats_text函数，参数类型错误',type(err))
    else:
        stats_text_cn(check)
        stats_text_en(check)
    finally:
        print("executing finally stats_text!") 