

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
        from collections import Counter  #引入counter模块，数数
        res2 = Counter(seg_list).most_common(100)
    return res2  
      

