#!/usr/bin/python

import string

def stats_text_en(en_text):
    for en_special_word in string.punctuation:
        if en_special_word in en_text:
            en_text = en_text.replace(en_special_word, "")

    en_word_count = {}
    en_text = en_text.split()
    for en_word in en_text:
        en_word_count.setdefault(en_word, 0)
        en_word_count[en_word] += 1

    en_sorted_words = sorted(en_word_count.items(), key=lambda obj: obj[1], reverse=True)

    return en_sorted_words


def stats_text_cn(cn_text):
    cn_special_words = "！“”#$%&‘’（）*+，-。/：；、……<=>？@[]「」《》^_`{|}~\n"
    for cn_special_word in cn_special_words:
        if cn_special_word in cn_text:
            cn_text = cn_text.replace(cn_special_word, "")

    cn_word_count = {}
    for cn_word in cn_text:
        cn_word_count.setdefault(cn_word, 0)
        cn_word_count[cn_word] += 1

    cn_sorted_words = sorted(cn_word_count.items(), key=lambda obj: obj[1], reverse=True)

    return cn_sorted_words


def stats_text(en_text, cn_text):
    #check the string is the type or error to popup
    if (not isinstance(en_text,str)) or (not isinstance(cn_text,str)):
        raise TypeError("string is ony the type can be accepted")

    print("EN words result: ", stats_text_en(en_text))
    print("CN words result: ", stats_text_cn(cn_text))