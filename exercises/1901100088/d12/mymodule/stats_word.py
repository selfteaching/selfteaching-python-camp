from collections import Counter
import jieba


def stats_text_cn(text,count):
    """Calculate the occurrence number of the chinese word.
    """

    text_c = []
    for d in text:
        if '\u4e00' <= d <= '\u9fff':
            text_c.append(d)
    text_d = "".join(text_c)
    text_d = jieba.cut(text_d, cut_all=False)
    text_e = []
    for td in text_d:
        if len(td)>1:
            text_e.append(td)
    r = Counter(text_e).most_common(count)
    return(r)


def stats_text_en(text,count):
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
    r = Counter(word).most_common(count)
    return(r)
    


def stats_text(text,count):
    """Calculate the occurrence number of the word both in english and chiness.
    """

    if type(text) == str and type(count) == int:
        return(stats_text_en(text,count)+stats_text_cn(text,count))
    else:
        raise ValueError('参数类型错误，需传入字符串及整数参数')