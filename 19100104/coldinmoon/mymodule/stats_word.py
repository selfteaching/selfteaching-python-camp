#1.封装统计英文词频的函数
#2.封装统计中文词频的函数
#Date:3/23/2019

dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}


def stats_text_en(text):   #创建一个名为stats_text_en的函数
        """统计英文词频的函数"""
        if isinstance(text,str):
            import re
            text = re.sub("[^A-Za-z]", " ", text.strip())   #只保留英文
            list1 = re.split(r"\W+",text)   #将字符串text转换为列表list1,只保留单词为list1中的元素
            while '' in list1:   #删除list1中为空的列表元素
                    list1.remove('')
                    for i in list1:   
                            dict1.setdefault(i,list1.count(i))  #将列表中的单词及单词的出现次数，分别赋值给dict1的键和值
                            tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   #将dict1按照value值从大到小排列，并将结果赋给元组tup1
                    for tup1 in tup1:   
                            dict2[tup1[0]] = dict1[tup1[0]]  
            return dict2
        else:ValueError('Input should be string')

def stats_text_cn(text):
    """统计中文词频的函数""" #使用文档字符串添加注释说明
    if isinstance(text,str):
         countcn={}
         for i in text:
                 if u'\u4e00'<= i <= u'\u9fff':
                         countcn[i]=text.count(i)
                         countcn=sorted(countcn.items(),key=lambda item:item[1],reverse=True)
                         return countcn
    else:ValueError('Input should be string')
    

#1.添加名为stats_text的函数，实现功能：分别调用stats_text_en , stats_text_cn，输出合并词频统计结果
#2.为stats_text添加注释说明
#Date:3/24/2019

def stats_text(text):
        """调用统计英文词频和中文词频的函数，合并词频统计结果"""
        if isinstance(text,str):
                return stats_text_en(text),stats_text_cn(text)
        else:ValueError('Input should be string')
