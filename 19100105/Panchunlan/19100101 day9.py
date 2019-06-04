
import collections
import re

def stats_text_en(en,count) :
    ''' 1. 英文词频统计。
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(en) == str : 
            text_en = re.sub("[^A-Za-z]", " ", en.strip())
            enList = text_en.split( )
            return collections.Counter(enList).most_common(count)
    else : 
            raise ValueError ('type of argumengt is not str')

def stats_text_cn(cn,count) :
    ''' 1. 汉字字频统计 
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(cn) == str : 
            cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
            cnString = ''.join(cnList)
            return collections.Counter(cnString).most_common(count)
    else :
            raise ValueError ('type of argumengt is not str')

def stats_text(text_en_cn,count_en_cn) :
    ''' 1. 合并英汉词频统计 
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(text_en_cn) == str : 
            return (stats_text_en(text_en_cn,count_en_cn)+stats_text_cn(text_en_cn,count_en_cn))
    else :
            raise ValueError ('type of argumengt is not str')
            

import mymodule.stats_word
import codecs

fileHandler = open('tang300.json', mode='r', encoding='UTF-8')
report_lines = fileHandler.readlines()
log = "".join(report_lines)
mymodule.stats_word.stats_text_cn(log)

counter=100
print("""---唐诗300首中词频最高的前100个字---""")
