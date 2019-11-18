def stats_text_en(text):#封装统计英⽂文单词词频的函数
    if not isinstance(text,str): 
        raise ValueError ("please input string type!") 
    text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    text=text.split()
    dict_test={}
    for i in text:  
        count=text.count(i)
        r1={i:count}
        dict_test.update(r1)
    return sorted(dict_test.items(),key=lambda x:x[1],reverse=True)

def stats_text_cn(text):#封装统计中文文单词词频的函数
    if not isinstance(text,str): 
        raise ValueError ("please input string type!") 
    cn_words = []
    for word in text:        
        if '\u4e00' <= word <= '\u9fff':
            cn_words.append(word)
    counter = {}
    cn_word_set = set(cn_words)
    for word in cn_word_set:
        counter[word] = cn_words.count(word)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

def stats_text(text):#实现功能：分别调⽤用stats_text_en , stats_text_cn ，输出合并词频统计结果
    if not isinstance(text,str): 
        raise ValueError ("please input string type!")     
    link_word_1 = stats_text_en(text)
    link_word_2 = stats_text_cn(text)
    link_word = link_word_1 + link_word_2
    return link_word

