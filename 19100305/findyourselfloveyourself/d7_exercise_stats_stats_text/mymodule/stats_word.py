import collections
import re

def stats_text_en(en) :
    text_en = re.sub("[^A-Za-z]", " ", en.strip())
    enList = text_en.split( )
    return collections.Counter(enList)

    
def stats_text_cn(cn) :
    cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
    cnString = ''.join(cnList)
    return collections.Counter(cnString)

def stats_text(text_en_cn) :
    return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))