
from collections import Counter
import re
import jieba
import json
import requests
import getpass
import yagmail
from pyquery import PyQuery 
import matplotlib.pyplot as plt
import numpy as np
def stats_text_en (text,count):
    text,count=checktype(text,count)
    temp=text.replace(',','').replace('.','').replace('*','').replace('!','').replace(':','').replace('\n',' ').replace('\t','').replace('，','').replace('。','').replace('！','').replace('？','').strip().lower() #把特殊符号都去掉，并全部换成小写
    dit_en={}
    list_en = temp.split(' ') #把字符串变为列表
    max = 0
    maxkey = ""
    for item in list_en:
        if (dit_en.get(item)):
            dit_en[item] = dit_en[item] + 1 #如果读入的每个单词作为key存在对应的值，则累加
        else:
            dit_en[item] = 1 #如果读入的单词作为key没有找到对应的值，则赋值为1
        if (dit_en[item] > max): #如果每个单词的统计数大于最大值，则重新赋值给最大值，并把对应的key赋值给maxkey
            max = dit_en[item]
            maxkey = item
    result_en=sorted(dit_en.items(),key=lambda x:x[1],reverse=True)[:count] #按照value的值，从大到小排序
    return result_en

  # -*- coding: utf-8 -*- 
def stats_text_cn (text,count):
    text,count=checktype(text,count)
    item=text.replace('，','').replace('。','').replace('！','').replace('？','').replace('\n','').replace('\t','').replace(' ','') #去掉特殊符号
    seg_list = jieba.lcut(item, cut_all=False)
    seg_list_4=list(filter(lambda s:len(s) >1,seg_list))
#     print(seg_list_4)
    return(Counter(seg_list_4).most_common(count))



def stats_text(text,count):
    text,count=checktype(text,count)
    list_cn=[]     
    for char in text:
        if (char >= u'\u4e00' and char<=u'\u9fa5') or (char >= u'\u0041' and char<=u'\u005a') or (char >= u'\u0061' and char<=u'\u007a') or (char >= u'\u0030' and char<=u'\u0039'): #判断一个字符是否为标点符号
            if char >= u'\u4e00' and char<=u'\u9fa5' :#如果是中文，则统一放进list_cn中，标点符号全部去掉
                list_cn.append("".join(char))  
            else: #如果是数字和字母，则统一放进list_en中，标点符号全部去掉
                continue #如果是汉字，就把汉字逐个放进list_cn中
        else: 
            continue
    for t in range(len(list_cn)):
        w1=list_cn[t]
        text=text.replace(w1,'').replace(',','').replace('.','').replace('*','').replace('!','').replace(':','').replace('\n',' ').replace('\t','').replace('，','').replace('。','').replace('！','').replace('？','').replace('“”','').strip()
    text_cn= "".join(list_cn)
    seg_list_cn = jieba.lcut(text_cn, cut_all=False)
    seg_list_cn_4=list(filter(lambda s:len(s) >1,seg_list_cn))
    list_en=text.split(" ")
#     print (list_en)
    result_list=Counter(seg_list_cn_4).most_common(count)
    return result_list


def checktype(x,count):
    if not isinstance(x,str):
        raise ValueError('input a string!')
    elif not isinstance(count,int):
        raise ValueError('input a int!')
    else:
        return x,count
def plot_wordsfreq(response,count):
    filename="./bar.png"

    document = PyQuery(response.text)
    content_input = document('#js_content').text()
    result_str = stats_text(content_input,count)
    list_words = [x[0] for x in result_str]
    list_freq=[x[1] for x in result_str]

    # 设置中文字体和负号正常显示
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False

    freq=list_freq
    plt.barh(range(count), freq, height=0.7, color='steelblue', alpha=0.8)  
    plt.yticks(range(count), list_words)
    plt.xlim(list_freq[count-1],list_freq[0])
    plt.xlabel("frequency")
    plt.title('top word frequency of this article')

    for x,y in enumerate(freq):
        plt.text(y+0,x,"%s"%y,va='center')
    plt.savefig(filename)
#     plt.show()

    return filename
    