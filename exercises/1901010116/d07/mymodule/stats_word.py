#封装统计英文单词词频的函数
import string
import re

def stats_text_en(text):
    text = re.sub('[^A-Za-z]',' ',text) #筛选英文单词，剔除其他文字
    text = text.lower().split()  #转换成小写，拆分字符串

    t_dict = {} #定义一个字典
    t_dict = t_dict.fromkeys(text)  #去掉重复单词

    #统计单词出现次数
    for i in t_dict.keys():
        t_dict[i] = text.count(i)
    
    #返回一个按词频降序排列的数组
    f = sorted(t_dict.items(),key = lambda t:t[1],reverse = True)
    return f


#封装统计中文汉字字频的函数
def stats_text_cn(text):
    text = re.sub(r'[^\u4E00-\u9FA5]','',text) #只留下汉字，剔除其他字符

    t_dict = {} #定义一个字典
    t_dict = t_dict.fromkeys(text)  #去掉重复汉字

    #统计汉字出现次数
    for i in t_dict.keys():
        t_dict[i] = text.count(i)
    
    #返回一个按词频降序排列的数组
    f = sorted(t_dict.items(),key = lambda t:t[1],reverse = True)
    return f

#分别调⽤stats_text_en , stats_text_cn ，输出合并词频统计结果
def stats_text(text):
    """
    统计英文单词及中文汉字出现的频次
    
    参数为字符串
    返回一个数列
    """
    return stats_text_en(text) + stats_text_cn(text)
