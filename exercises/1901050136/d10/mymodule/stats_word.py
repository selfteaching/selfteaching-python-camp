import collections
import jieba

# this script is to learn  call Library from others

# 1 for english word
def stats_text_en(text):
    # judge if the type of input is correct.
    if type(text) != str:
        raise ValueError('The input text is not the type of String')

    text = text.strip().split()# for chinese words dividing
    words = [] # for store the text after processing
    symbols = '、??:「」，。.!,“”' ' \n '
    for word in text:
        for  symbol in symbols:
            word = word.replace(symbol,'') # delet the redundant symbols in the text
        words.append(word)

    # the collections is used in stead of set and dictionary
    cnt = collections.Counter()
    for word in words:
        if len(word):
            cnt[word] += 1
    Result = cnt
    count = len(Result)

    return Result, count


# 2 for chinese word **this version is to implement statstics for words rather than single Han Chars**
def stats_text_cn(text):

    # judge if the type of input is correct.
    if type(text) != str:
        raise ValueError('The input text is not the type of String')

    # delete the non-chinese character
    text_cn = ''
    for character in text:
        if '\u4e00'<= character <= '\u9fff':
            text_cn += character
    text = text_cn # new text without non-chinese chars

    # dividing words using jieba
    words = jieba.cut(text)
    text = (' '.join(words))
    
    # select the words whose length >= 2
    text_list = text.split()
    characters_cn = [] # for storing all the words larger 2
    for chars in text_list:
        if len(chars) >= 2:
            characters_cn.append(chars)
    
    # the collections is used in stead of set and dictionary
    cnt = collections.Counter()
    for word in characters_cn:
        if len(word):
            cnt[word] += 1

    Result = cnt
    count = len(Result)

    return Result, count

# 3 the function which calls the above 2 functions
def stats_text(text):

    # judge if the type of input is correct.
    if type(text) != str:
        raise ValueError('The input text is not the type of String')

    # for chinese words
    Result_cn = stats_text_cn(text)[0]
    count_cn = stats_text_cn(text)[1]

    # for english words
    # remove of the chinese characters in the text
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            text = text.replace(character,'')
    Result_en = stats_text_en(text)[0] # text is non-chinese text
    count_en = stats_text_en(text)[1]

    Result = Result_cn + Result_en # collections + collections
    count = count_cn + count_en

    return Result,count