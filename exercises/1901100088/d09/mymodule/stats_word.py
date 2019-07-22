from collections import Counter


def stats_text_cn(text,count):
    """Calculate the occurrence number of the chinese word.
    """

    if type(text) == str:
        text_c = []
        for d in text:
            if '\u4e00' <= d <= '\u9fff':
                text_c.append(d)
        r = Counter(text_c).most_common(count)
        return(r)
    else:
        raise ValueError('参数类型错误，需传入str')


def stats_text_en(text,count):
    """Calculate the occurrence number of the english word.
    """

    if type(text) == str:
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
    else:
        raise ValueError('参数类型错误，需传入str')
    


def stats_text(text,count):
    """Calculate the occurrence number of the word both in english and chiness.
    """

    if type(text) == str:
        return(stats_text_en(text,count)+stats_text_cn(text,count))
    else:
        raise ValueError('参数类型错误，需传入str')
