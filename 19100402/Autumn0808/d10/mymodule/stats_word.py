import collections
import re
import jieba

def stats_text_en(en,count) :
    if type(en) == str : 
            text_en = re.sub("[^A-Za-z]", " ", en.strip())
            enList = text_en.split( )
            return collections.Counter(enList)
            ###英文单词词频统计
    else : 
            raise ValueError ('type of argumengt is not str')
            ###参数类型检查，不为字符串抛出异常

def stats_text_cn(cn,count) :
    if type(cn) == str : 
            cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
            cnString = ''.join(cnList)
            segList = jieba.cut(cnString,cut_all=False)
            cnnewList = []
            for i in segList:
                    if len(i) >= 2:
                            cnnewList.append(i)
                    else:
                            pass
            countList = collections.Counter(cnnewList).most_common(count)        
            return countList
            ###汉字字频统计
    else :
            raise ValueError ('type of argumengt is not str')
            ###参数类型检查，不为字符串抛出异常

def stats_text(text_en_cn,count_en_cn) :
    if type(text_en_cn) == str : 
            return (stats_text_en(text_en_cn,count_en_cn)+stats_text_cn(text_en_cn,count_en_cn))
            ###中英文合并词频统计
    else :
            raise ValueError ('type of argumengt is not str')
            ###参数类型检查，不为字符串抛出异常
