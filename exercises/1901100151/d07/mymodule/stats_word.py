def stats_text_en(text):
    """
    统计英⽂单词词频的函数
    """
    a_text = text.split()
    b_words = []
    c_text = ".,!?*-"
    for d_text in a_text:
        for e_text in c_text:
            d_text = d_text.replace(e_text,"")
            # error: 函数replace没有拼对。
        # error: d_text名称前后没有保持一致。
        if len(d_text) and d_text.isascii():
            b_words.append(d_text)
    f_dict = {}
    h_set = set(b_words)
    for g_word in h_set:
        f_dict[g_word] = b_words.count(g_word)
        # error：对f_dict[]中对“f_divt”没有理解，错写为f[]。
    return sorted(f_dict.items(), key = lambda x: x[1],reverse = True)

def stats_text_cn(text):
    """
    统计中⽂汉字字频的函数
    """
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    a_dict = {}
    b_set = set(cn_characters)
    for c_character in b_set:
        a_dict[c_character] = cn_characters.count(c_character)
    return sorted(a_dict.items(), key = lambda x: x[1], reverse = True)

def stats_text(text):
    """
    综合统计英⽂单词词频和中⽂汉字字频的函数
    """
    # a_text = stats_text_en(text) + stats_text_cn(text)
    # print(a_text)
    return stats_text_en(text) + stats_text_cn(text)

# en_text = '''
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# '''

# cn_text = '''
# 封装统计英⽂文单词词频的函数,封装统计中⽂文汉字字频的函数.
# '''

# text = '''
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# 封装统计英⽂文单词词频的函数,封装统计中⽂文汉字字频的函数.
# '''

# if __name__ == '__main__':
    # en_result = stats_text_en(en_text)
    # cn_result = stats_text_cn(cn_text)
    # print("统计英⽂文单词词频的函数\n:",en_result)
    # print("统计中⽂文汉字字频的函数\n:",cn_result)
    # print("stats_text_en和stats_text_cn合并词频统计的函数:\n",stats_text(text))
