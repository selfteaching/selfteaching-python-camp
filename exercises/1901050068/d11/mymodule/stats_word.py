

# #定义函数
def stats_text_cn(text):
    """This is for the article written in Chinese
    """
    if type(text) != str:
        raise ValueError('This is a wrong type')
    else:
        import re
        text = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", " ", text)
        t1 = text.replace(" ","")

        #jieba分词
        import jieba
        seg_list = jieba.cut(t1,cut_all=False)
        v = set(seg_list)
        long_words = [w for w in v if len(w)>=2]    #细粒度选择词
        from collections import Counter  #引入counter模块，数数
        res2 = Counter(long_words)
        d = dict(res2)    #变成dict
        d2 = sorted(d.items(),key=lambda a: a[1],reverse=True)
        for i in range(20):    #排序
            print(d2[i])
    return(d2[i])     
      

