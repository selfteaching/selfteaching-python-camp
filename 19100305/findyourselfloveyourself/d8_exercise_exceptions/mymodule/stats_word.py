import collections
import re

def stats_text_en(en) :
    if type(en) == str:
            text_en = re.sub("[^A-Za-z]", " ", en.strip())
            enList = text_en.split( )
            return collections.Counter(enList)
    else:
            raise ValueError('type of argumengt is not sor')
    
def stats_text_cn(cn) :
    if type(cn) == str :
            cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
            cnString = ''.join(cnList)
            return collections.Counter(cnString)
    else :
            raise ValueError('type of argumengt is not str')
def stats_text(text_en_cn) :
    if type(text_en_cn) == str :
            return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))
    else :
            raise ValueError('type of argumengt is not str')