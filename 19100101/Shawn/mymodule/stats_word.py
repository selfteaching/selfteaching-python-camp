import collections
import re
def stats_text_en(text_en):
        entext = re.sub("[^A-Za-z]", " ", text_en.strip())
        entext = entext.split()
        return collections.Counter(entext)
    
#汉字词频统计
def stats_text_cn(text_cn):
   cntext = re.findall(u'[\u4e00-\u9fff]+', text_cn.strip())
   newString = ''.join(cntext)
   return collections.Counter(newString)
# 合并英汉词频统计 '''
def stats_text(text_en_cn) :
    return (stats_text_en(text_en_cn)+stats_text_cn(text_en_cn))
    

