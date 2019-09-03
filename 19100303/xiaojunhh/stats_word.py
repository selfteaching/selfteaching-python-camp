import collections
import re
import jieba

def stats_text_en(en,count):
    '''1.英文词频统计
       2.参数类型检查，不为字符串则提示错误
    '''
    if type(en) == str :
        text_en =re.rub("[^A-Za-z]","",en.strip())
        enList = text_en.split()
        return collections.Counter(enList).most_common(count)
    else :
        raise ValueError("输入内容不是字符串")

def stats_text_cn(cn.count):
    '''1.中文词频统计
       2.参数类型检查，不为字符串则提示错误
    '''
    if type(cn) == str:
        cnList = re.findall(u'[\u4e00-\u9fff+',cn.srrip())
        cnString = ''.join(cnList)
        segList = jieba.cut(cnString,cut_all=False)
        cnnewList = []
        for i in segList:
            if len(i) >= 2:
                cnnewList.append(i)
            else:
                pass
        countList = collections.Counter(cnnewList).most_common
        return countList
    else :
        raise ValueError('舒服内容不是字串')
def stats_text(text_en,count_en_cn):
    '''1.合并中英文词频统计
       2.参数类型检查，不为字符串则提示错误
    '''
    if type(text_en_cn,count_en_cn):
        return(stats_text_en(text_en_cn,count_en_cn)+stats_text_cn(text_en_cn,count_en_cn))
    else:
        raise ValueError('输入内容不是字符串')



