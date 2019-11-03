def stats_text_en(text):
    """Count English word frequency of input text"""
    text = text.replace(',','') 
    text = text.replace('.','') 
    text = text.replace('!','') 
    text = text.replace('?','') 
    text = text.replace('-','') 
    text = text.replace('*','') 
    text = text.replace(';','') 
    text = text.replace(':','') 
    text = text.replace('\"','') 
    text = text.replace('\'','') 
    l = text.split()
    from collections import Counter
    d = Counter(l)
    return d
 
def stats_text_cn(text):
    """Count Chinese word frequency of input text"""
    l = []
    for i in text:
        if '\u4e00' <= i <= '\u9fff':
            l.append(i)
    from collections import Counter
    d = Counter(l)
    return d