#1.封装统计英文词频的函数
#2.封装统计中文词频的函数
#Date:3/23/2019

#1.使用标准库中的Counter完善stats_word中的，中英文词频统计的排序功能，使函数能够按照词频的次序有序输出
#2.分别给两个函数添加一个int变量count，用于限制输出元素的个数
#Date:3/26/2019



import re
import collections

def stats_text_en(text,n):   #创建一个名为stats_text_en的函数
        """统计英文词频的函数"""
        if isinstance(text,str):
            counten={}
            text = re.sub("[^A-Za-z]", " ", text.strip())   #只保留英文
            counten = re.split(r"\W+",text)   #将字符串text转换为列表counten,只保留单词counten中的元素
            while '' in counten:   #删除list1中为空的列表元素
                    counten.remove('')
            s=collections.Counter(counten)      #使用标准库中的Counter完善词频统计排序功能
            return s.most_common(n)     #添加一个int变量count，用于限制输出元素的个数
        else:ValueError('Input should be string')

#1.通过jieba精确模式将stats_word.py中stats_text_cn函数的输入字符串进行分词
#2.统计分词后的词频（中文只统计长度大于等于2的词）
#3.输出tang300.json文件中的词频前20的词和词频数
#Date:3/27/2019

import jieba
import collections

def stats_text_cn(text,n):
        """jieba分词后，统计长度大于等于2的中文词频"""
        if isinstance(text,str):        #若输入非字符串，显示异常
                count=[]
                countcn=[]
                n=int(n)        #添加一个int变量count，用于限制输出元素的个数
                count=jieba.cut(text,cut_all=False)     #通过jieba精确模式对输入字符串进行分词
                for i in count:
                        if u'\u4e00'<= i <=u'\u9fff':   #只统计中文
                                if len(i) >= 2:  #只统计中文只统计长度大于等于2的词
                                        countcn.append(i)
                return collections.Counter(countcn).most_common(n)      #使用标准库中的Counter完善词频统计排序功能
        else: ValueError('Input should only be  string')

#1.添加名为stats_text的函数，实现功能：分别调用stats_text_en , stats_text_cn，输出合并词频统计结果
#2.为stats_text添加注释说明
#Date:3/24/2019

def stats_text(text,n):
        """调用统计英文词频和中文词频的函数，合并词频统计结果"""
        if isinstance(text,str):
                return stats_text_en(text,n),stats_text_cn(text,n)
        else:ValueError('Input should be string')