#d9 excercise
import collections
import re
import jieba
#英文字频统计
def stats_text_en(text_en,count):
        if type(text_en) == str:
                entext = re.sub("[^A-Za-z]", " ", text_en.strip())
                enList = entext.split()
                return collections.Counter(enList).most_common(count)
        else:
                raise ValueError ('it is not str')
    
#汉字词频统计
def stats_text_cn(text_cn,count):
        if type(text_cn) == str:
                cntext = re.findall(u'[\u4e00-\u9fff]+', text_cn.strip())
                newString = ''.join(cntext)
                cnString = jieba.cut(newString,cut_all=False)
                cnList = []
                for i in cnString:
                          if len(i) >= 2:
                                cnList.append(i)
                          else:
                                pass         
                return collections.Counter(cnList).most_common(count)
        else:
                raise ValueError ('it is not str')
# 合并英汉词频统计 '''
def stats_text(text_en_cn,count_en_cn) :
        if type(text_en_cn) == str:
                return (stats_text_en(text_en_cn,count_en_cn)+stats_text_cn(text_en_cn,count_en_cn))
        else :
                raise ValueError('it is not str')
    

