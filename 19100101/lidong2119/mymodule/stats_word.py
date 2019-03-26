import collections
import re

def stats_text_en(en):
    '''1.英文词频统计
       2.参数类型检查，不为字符串则提示错误
    '''
    if type(en) == str :
        text_en =re.sub("[^A-Za-z]"," ",en.strip())
        enList = text_en.split( )
        return collections.Counter(enList)
    else :
        raise ValueError('输入内容不是字符串')

def stats_text_cn(cn):
    '''1.中文词频统计
       2.参数类型检查，不为字符串则提示错误
    '''
    if type(cn) == str:
        cnList = re.findall(u'[\u4e00-\u9fff]+',cn.strip())
        cnString = ''.join(cnList)
        return collections.Counter(cnString)
    else :
        raise ValueError('输入内容不是字符串')

def stats_text(text_en_cn):
    '''1.合并中英文词频统计
       2.参数类型检查，不为字符串则提示错误
    '''
    if type(text_en_cn) == str:
        return(stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))
    else:
        raise ValueError('输入内容不是字符串')