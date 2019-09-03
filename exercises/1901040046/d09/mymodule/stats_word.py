#将字符串s按照None的分隔切分为一个字符串组，并清洗字符串元素的标点符号，并统计不同字符是数量，最后以数量降序排列。
import collections
import re
def stats_text_en(en,count):
    if type(en) == str:#新增类型检查语句
       text_en = re.sub("[^A-Za-z]"," ",en.strip())
       enList = text_en.split()
       return collections.Counter(enList).most_common(count)
    else:
       raise ValueError("输入不为字符串")


#定义一个用来统计汉字的函数.新增list函数将中文字符串切分。
def stats_text_cn(cn,count):
        if type(cn) == str:#新增类型检查语句 
           cnList = re.findall(u'[\u4e00-\u9fff]+',cn.strip())
           cnString = ''.join(cnList)
           return collections.Counter(cnString).most_common(count)
        else:
           raise ValueError("输入不为字符串")



def stats_text(text_e_c,count_e_c):#定义函数用来统计并打印中英文字符以及对应数量。
    if type(text_e_c) == str:
       return(stats_text_en(text_e_c,count_e_c)+stats_text_cn(text_e_c,count_e_c))
    else:
       raise ValueError("输入不为字符串")
