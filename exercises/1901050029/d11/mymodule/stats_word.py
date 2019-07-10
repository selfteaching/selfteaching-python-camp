# Filename : stats_word.py
# author by : 张金磊



from collections import Counter
from pandas import Series
import re
import jieba 


#定义函数用于去除英文文本中的其他字符（!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~）和中文
def getText(text):
    txt = text
    txt = txt.lower()
    result = re.sub("[^A-Za-z]", " ", txt.strip())
    for ch in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~':
        result = result.replace(ch, " ")
    return result

#定义函数用于统计英文单词词频，并按词频降序输出 
def stats_text_en(text, count=100):
    if not isinstance(text, str):
        raise  ValueError('the type of argument need str')
        
    hamletTxt = getText(text)
    words = hamletTxt.split()
    word = Counter(words)      #  It is an unordered collection where 
    word = word.most_common(count)
#    word = Series(word)        #  elements are stored as dictionary keys and  their counts are stored as dictionary values.
#    word =  word.sort_values(ascending=False)                         
   
    print('英文单词词频统计结果： ', word) 
    return word
             
    
#定义函数用于统计中文汉字字频，并按字频降序输出
def stats_text_cn(text, count):
    if not isinstance(text, str):
        raise  ValueError('the type of argument need str')
        
    result = re.findall(u'[\u4e00-\u9fff]+', text)    #汉字的unicode范围
    words = ''.join(result)
    seg_list = jieba.cut(words,cut_all=False)
    temp = []
    for i in seg_list:
        if len(i) > 1:
            temp.append(i)
    word = Counter(temp).most_common(count)
#    word = Series(word)
#    word =  word.sort_values(ascending=False)
           
    print('汉字词频统计结果： ', word)   
    return word

    
#输出中英文合并词频统计结果
def stats_text(text, count=100):    
    if not isinstance(text, str):
        raise  ValueError('the type of argument need str')
        
    stats_text_en(text, count)
    print('\n')
    stats_text_cn(text, count)

   


