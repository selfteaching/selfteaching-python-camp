import collections  #集合 模块：该模块实现了专门的容器数据类型，提供了Python的通用内置容器，dict，list，set和tuple的替代方法。
import re           #重新  模块：提供与Perl中类似的正则表达式匹配操作。 它支持8位和Unicode字符串; 模式和正在处理的字符串都可以包含空字节和US ASCII范围之外的字符。
import jieba

def stats_text_en(en) :
    ''' 英文词频统计'''
    text_en = re.sub("[^A-Za-z]", " ", en.strip())
    enList = text_en.split( )
    return collections.Counter(enList).most_common(100)

    
def stats_text_cn(cn) :
    ''' 汉字字频统计 '''
    cnList = re.findall(u'[\u4e00-\u9fa5]+', cn.strip())
    cnString = ''.join(cnList)
    
    segList = jieba.cut(cnString,cut_all=False)
    SHList = {}
    for i in segList :
          if len(i) >= 2 :
               SHList[i] = cnString.count(i)
          else :
               pass       

    return collections.Counter(SHList).most_common(10)

def stats_text(text):
    ''' 合并英汉词频统计 '''
    if type(text) ==str:
         return (stats_text_cn(text))
    else:
         raise ValueError ('this is not Valid Character')