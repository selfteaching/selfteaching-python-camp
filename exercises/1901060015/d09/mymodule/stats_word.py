
def stats_text_en(text):
    # 文章字符串前期处理,分割英文
    
    t=text.split()
    from collections import Counter
    t1=Counter(t).most_common(100)
    return t1


   


def stats_text_cn(text):
    # 文章字符串前期处理
    
    from collections import Counter
    import jieba
    #分割汉字
    t=jieba.lcut(text)
    #计数
    t1=Counter(t).most_common(100)
    return t1


def stats_text(text):
    #参数类型检查
    if not isinstance(text,(str)):
        raise TypeError('ValueError')
        

    return stats_text_cn(text)+stats_text_en(text)














       



