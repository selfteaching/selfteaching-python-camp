
import re
from collections import Counter
import jieba

    
def stats_text_en(text,count):
    '''This function aims to count English words.'''

    if type(text) == str:
        result = re.sub("[^A-Za-z]", " ", text.strip())
        newList = result.split()
        return (Counter(newList).most_common(count),'\n')
    else:
        raise ValueError(type(text)) 

def stats_text_cn(text,count):
    ''' This function aims to count Chinese words.'''

    if type(text) == str:
        result1 = re.findall(u'[\u4e00-\u9fff]+',text)
        newString = ''.join(result1)
        b= jieba.cut(newString)
        newString1 = []
        for i in b:
            if len(i)>=2:
                newString1.append(i)
        return (Counter(newString1).most_common(count),'\n')
    else:
        raise ValueError(type(text))

def stats_text(text,count):
     return (stats_text_en(text,count),stats_text_cn(text,count))
    



    


