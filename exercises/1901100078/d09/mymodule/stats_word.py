from collections import Counter

def stats_text_en(text, count):
    ''' count the word in the text '''
    if not isinstance(text, str):
        raise ValueError('参数必须是str类型，输入类型%s' %type(text))
    words_list = text.split()
    no_pun_list = []
    for word in words_list:
        word = word.strip('.!--*')
        if word.isalpha():
            no_pun_list.append(word)
    
    words_seq = Counter(no_pun_list).most_common(count)
    return words_seq


def stats_text_cn(text, count):
    '''统计中文字频'''
    if not isinstance(text, str):
        raise ValueError('Sould be str type, input %s'%type(text))
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    
    cn_seq = Counter(cn_characters).most_common(count)
    return cn_seq

def stats_text(text, count):
    "统计文本中出现的英文以及中文字符频率"
    if not isinstance(text, str):
        raise ValueError('not str type, input tyoe is %s'%type(text))
    
    return stats_text_en(text, count) + stats_text_cn(text, count)
    
    
if __name__ == '__main__':
    text = '''learn python is very funny, 但是没想象中那么轻松。'''
    print(stats_text(text,100))


    