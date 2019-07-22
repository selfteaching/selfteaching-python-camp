
import re
from collections import Counter

    
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
        result1 = re.findall(u'[\u4e00-\u9fff]+', text.strip())
        newString = ''.join(result1)
        return (Counter(newString).most_common(count),'\n')
    else:
        raise ValueError(type(text))

def stats_text(text,count):
     return (stats_text_en(text,count),stats_text_cn(text,count))
    



    


