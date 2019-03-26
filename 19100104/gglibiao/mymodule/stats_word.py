
import collections
import re           #引入正则表达式

def stats_text_en(en) :
    ''' 英文词频统计'''
    text_en = re.sub("[^A-Za-z]", " ", en.strip())     #re.sub  替换字符串中的匹配项。利用正则表达式去掉英文以外的字符以及空格
    enList = text_en.split( )
    return collections.Counter(enList)

    
def stats_text_cn(cn) :
    ''' 汉字字频统计 '''
    cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
    cnString = ''.join(cnList)
    return collections.Counter(cnString)

def stats_text(text_en_cn) :
    ''' 合并英汉词频统计 '''
    return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))