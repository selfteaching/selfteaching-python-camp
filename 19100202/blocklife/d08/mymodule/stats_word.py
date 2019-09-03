import collections
import re

def stats_text_en(en) :
    ''' 英文词频统计'''
    if type(en) != str:
        raise ValueError ("This is not an str type")
    text_en = re.sub("[^A-Za-z]", " ", en.strip())
    enList = text_en.split( )
    return collections.Counter(enList)

    
def stats_text_cn(cn) :
    ''' 汉字字频统计 '''
    if type(cn) != str:
        raise ValueError ("This is not an str type")
    cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
    cnString = ''.join(cnList)
    return collections.Counter(cnString)

def stats_text(text_en_cn) :
    ''' 合并英汉词频统计 '''
    if type(text_en_cn) != str:
        raise ValueError ("This is not an str type")
    return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))