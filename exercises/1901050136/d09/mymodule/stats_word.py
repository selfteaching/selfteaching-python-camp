import collections

# this script is to learn standard Library

# 1 for english word
def stats_text_en(text):
    # judge if the type of input is correct.
    if type(text) != str:
        raise ValueError('The input text is not the type of String')

    text = text.strip().split()
    words = [] # for store the text after processing
    symbols = '、??:「」，。.!,“”' ''
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


# 2 for chinese word
def stats_text_cn(text):
    # judge if the type of input is correct.
    if type(text) != str:
        raise ValueError('The input text is not the type of String')

    characters_cn = [] # for storing the text after processing

    for character in text:
        if '\u4e00'<= character <= '\u9fff':
            characters_cn.append(character)
    
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