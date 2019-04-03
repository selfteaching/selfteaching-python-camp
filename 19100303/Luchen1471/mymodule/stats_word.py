# this is d8 excercise for errors and exceptions
# date : 2019.3.25
# author by : qiming
# Luchen：延用上次作业，完善本次内容。+1


import collections
import re
import jieba


def stats_text_en(en,x): #还没找到方法限制x为int
    ''' 1. 英文词频统计。
        2. 参数类型检查，不为字符串抛出异常。
    '''    
    if type(en) == str : 
            text_en = re.sub("[^A-Za-z]", " ", en.strip())
            enList = text_en.split( )
            return collections.Counter(enList).most_common(x)
    else : 
            raise ValueError ('type of argumengt is not str')

def stats_text_cn(cn): #还没找到方法限制y为int,这次把20这个参数内置了
    ''' 1. 汉字字频统计 
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(cn) == str : 
            #cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
            cnList = jieba.cut(cn)#默认精确模式
            cnList1 = []
            for i in cnList:
                    if len(i) >= 2:
                        cnList1.append(i)
            #cnString = ''.join(cnList)
            return collections.Counter(cnList1).most_common(20)
    else :
            raise ValueError ('type of argumengt is not str')


#def stats_text(text_en_cn) :
#    ''' 1. 合并英汉词频统计 
#        2. 参数类型检查，不为字符串抛出异常。
#    '''
#    if type(text_en_cn) == str : 
#            return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))
#    else :
#            raise ValueError ('type of argumengt is not str')

#print(stats_text_cn("我来到北京清华大学"))#试验成功
