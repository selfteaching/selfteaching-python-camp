import re
from collections import Counter

def stats_text_en(count,text):
    '''This function aims to count English words.'''

    if type(text)==str:
        result = re.sub("[^A-Za-z]", " ", text.strip())
        newList = result.split()
        return (Counter(newList).most_common(count),'\n')
    else:
        raise ValueError(type(text))

def stats_text_cn(count,text):
    ''' This function aims to count Chinese words.'''
    
    if type(text)==str:
        result1 = re.findall(u'[\u4e00-\u9fff]', text)
        newString = result1
        return (Counter(newString).most_common(count),'/n')
    else:
         raise ValueError(type(text))

def stats_text(text,count):
    return (stats_text_en(count,text),stats_text_cn(count,text))
