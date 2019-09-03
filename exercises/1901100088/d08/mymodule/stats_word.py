def stats_text_cn(text):
    """Calculate the occurrence number of the chinese word.
    """
    if type(text) == str:
        text_c = []
        for d in text:
            if '\u4e00' <= d <= '\u9fff':
                text_c.append(d)
        cw = []
        for c in text_c:
            cw.append(text_c.count(c))
        dic = dict(zip(text_c,cw))
        #dic.pop("\n")
        stat_cn = sorted(dic.items(),key=lambda item:item[1], reverse=True)
        return(stat_cn)
    else:
        raise ValueError('参数类型错误，需传入str')


def stats_text_en(text):
    """Calculate the occurrence number of the english word.
    """
    
    stat = text.lower()
    stats = stat.split()
    word = []
    puns= ',.*-!9'  
    for s in stats:
        for pun in puns:
            if pun in s:
                s = s.replace(pun,"")
        if len(s) and s.isalpha():
                word.append(s)
    count_word = []
    for cw in word:
        count_word.append(word.count(cw))
    dic = dict(zip(word,count_word))
    stat_en = sorted(dic.items(),key=lambda item:item[1], reverse=True)
    return(stat_en)
    


def stats_text(t):
    """Calculate the occurrence number of the word both in english and chiness.
    """

    if type(t) == str:
        return(stats_text_en(t)+stats_text_cn(t))
    else:
        raise ValueError('参数类型错误，需传入str')
