import collections

import re

import jieba #第三方库，结巴



def stats_text_en(t_en,count): 

    '''该函数返回一个英文单词词频统计，样式为（word,count）'''

    if type(t_en) == str:

        text_en = re.sub("[^A-Za-z]", " ", t_en)

        enlist = text_en.split() 

        return collections.Counter(enlist).most_common(count)

    else:

        raise ValueError("输入不为字符串")

        

def stats_text_cn(t_cn,count):

    '''该函数返回一个中文单词词频统计，样式为（word,count）'''

    if type(t_cn) == str:

        text_cn = re.findall(u'[\u4e00-\u9fff]+',t_cn)

        seg_list = jieba.cut(' '.join(text_cn)) # 精确模式seg_list = jieba.cut(" ", cut_all=False)

        cn_list = []

        for i in seg_list:

            if len(i) >= 2:

                cn_list.append(i)

        return collections.Counter(cn_list).most_common(count)

    else:

        raise ValueError('输入不为字符串')

        

def stats_text(en_cn,count):

    '''该函数返回一个英文单词词频+中文字频混合的函数'''

    if type(en_cn) == str:

        return (stats_text_en(en_cn,count)+stats_text_cn(en_cn,count))

    else:

        raise ValueError('输入不为字符串')