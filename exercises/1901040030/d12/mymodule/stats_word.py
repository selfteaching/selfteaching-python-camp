from collections import Counter
import re
import jieba
re_en = re.compile(r'[\u0061-\u007a,\u0020]') #用正常表达式获取所有的英文和空格，为了能达到单词需要保留空格
re_cn = re.compile(r'[\u4E00-\u9FA5]') #用正常表达式获取所有的汉字


def stats_text_cn (text:'输入的文本',count) -> list:
    if not isinstance(text,str):
        raise ValueError('stats_text_cn函数需要的参数是字符串')
    cn_text=''.join(re_cn.findall(text)) #正则表达式获取中文
    cn_text_list=jieba.lcut(cn_text) #使用lcut，分词后获得列表
    for i in cn_text_list: #遍历列表，删除长度小于2的元素
        if len(i) <=1:
            cn_text_list.remove(i)     
    count_cn=Counter(cn_text_list).most_common(count)#用counter统计列表的元素，用count限制个数
    return count_cn


def stats_text_en (text:'输入的文本',count) -> list:
    if not isinstance(text,str):
        raise ValueError('stats_text_en函数需要的参数是字符串')
    en_text=''.join(re_en.findall(text))  #截取英文和空格，拼接成带单词的字符串
    en_text_list=en_text.split() #截取出单词，存在列表里
    count_en=Counter(en_text_list).most_common(count)#用counter统计列表的元素，用count限制个数
    return count_en 

def stats_text (text:'输入的文本',count) -> list:
    text_list=stats_text_cn(text,count) #运行统计中文的函数
    text_list.extend(stats_text_en(text,count)) #运行统计英文的函数
    return text_list
