
import re

    
def stats_text_en(text):
    '''This function aims to count English words.'''

    if type(text) == str:
        result = re.sub("[^A-Za-z]", " ", text.strip())
        newList = result.split()
        a ={}
        for i in newList:
            a.update({i:newList.count(i)})
        a1= sorted(a.items(), key= lambda x:x[1],reverse = True)
        return a1
    else:
        raise ValueError(type(text)) 

def stats_text_cn(text):
    ''' This function aims to count Chinese words.'''

    if type(text) == str:
        result1 = re.findall(u'[\u4e00-\u9fff]+', text.strip())
        newString = ''.join(result1)
        b ={}
        for i in newString:
            b.update({i:newString.count(i)})
        b1 = sorted(b.items(),key = lambda x:x[1],reverse= True)
        return b1
    else:
        raise ValueError(type(text))

def stats_text(text):
     return (stats_text_en(text),stats_text_cn(text))
        


