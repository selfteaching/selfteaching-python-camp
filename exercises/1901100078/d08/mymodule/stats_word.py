def stats_text_en(text):
    ''' count the word in the text '''
    if not isinstance(text, str):
        raise ValueError
    words_list = text.split()
    no_pun_list = []
    for word in words_list:
        word = word.strip('.!--*')
        if word.isalpha():
            no_pun_list.append(word)
    words_dict = {}
    word_set = set(no_pun_list)
    for word in word_set:
        words_dict[word] = no_pun_list.count(word)
    words_seq = sorted(words_dict.items(), key = lambda x: x[1], reverse = True)
    return words_seq


def stats_text_cn(text):
    '''统计中文字频'''
    if not isinstance(text, str):
        raise ValueError
    List = [i for i in text]
    word_dict = {}
    for word in set(List):
        word_dict[word] = List.count(word)
    word_seq = sorted(word_dict.items(), key = lambda x: x[1], reverse = True)
    return word_seq

def stats_text(text):
    "统计文本中出现的英文以及中文字符频率"
    if not isinstance(text, str):
        raise ValueError
    cn_str = ''
    en_str = ''
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            cn_str += char
        else:
            en_str += char
    cn_result = stats_text_cn(cn_str)
    en_result = stats_text_en(en_str)
    return cn_result,en_result
    
    



    