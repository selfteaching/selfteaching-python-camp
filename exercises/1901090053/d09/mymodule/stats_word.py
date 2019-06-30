

def stats_text_en(text, count):
    ''' count the number of every English word in a text '''
    if type(text) is not str:
        raise ValueError('request input data type of parameter text is sting')
    if type(count) is not int:
        raise ValueError('request input data type of parameter count is int')
    
    text = text.lower()
    import re
    filtrate = re.findall(r'[^\u4E00-\u9FA5]',text)
    en_text = str()
    for item in filtrate:
        en_text = en_text + item
    en_text = re.findall(r'\w+', en_text)    
    import collections as col 
    d = col.Counter(en_text)
    d = d.most_common(count)
    d = dict(d)
    return d


 
def stats_text_cn(text, count):
    ''' count the number of every Chinese character in
    a text '''
    if type(text) is not str:
        raise ValueError('request input data type of parameter text is sting')
    if type(count) is not int:
        raise ValueError('request input data type of parameter count is int')    
      
    import re
    text_list = re.findall(r'([\u4e00-\u9fff])',text)
    import collections as col 
    d = col.Counter(text_list)
    d = d.most_common(count)
    d = dict(d)
    return d


def stats_text(text, count):
    ''' count the number of every Chinese character and English word in
    a text'''
    if type(text) is not str:
        raise ValueError('request input data type of parameter text is sting')
    if type(count) is not int:
        raise ValueError('request input data type of parameter count is int')    
    
    import collections as col
    t = {**stats_text_en(text, count), **stats_text_cn(text, count)}
    d = col.Counter(t)
    d = d.most_common(count)
    d = dict(d)
    return d
    

