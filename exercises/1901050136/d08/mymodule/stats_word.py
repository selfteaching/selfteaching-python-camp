# this script is to learn try except finally raise

# 1 for english word
def stats_text_en(text):
    # judge if the type of input is correct.
    if type(text)==str:
        pass
    else:
        raise ValueError('The input text is not the type of String')

    text = text.strip().split()
    words = [] # for store the text after processing
    symbols = '、??:「」，。.!,“”'
    for word in text:
        for  symbol in symbols:
            word = word.replace(symbol,'') # delet the redundant symbols in the text
        words.append(word)

    word_set = set(words) # transfer the list to the set
    counter_dict = {}
    for word in word_set: # count the number for each word
        counter_dict[word] = words.count(word)

    Result = sorted(counter_dict.items(),key = lambda x: x[1], reverse = True)

    return Result


# 2 for chinese word
def stats_text_cn(text):
    # judge if the type of input is correct.
    if type(text)==str:
        pass
    else:
        raise ValueError('The input text is not the type of String')

    characters_cn = [] # for storing the text after processing

    for character in text:
        if '\u4e00'<= character <= '\u9fff':
            characters_cn.append(character)
    characters_set = set(characters_cn) # transfer the list to the set

    counter_dict = {}

    for character in characters_set: # count the number for each word
        counter_dict[character] = characters_cn.count(character) # for a dict{key,value} this is: dict[key] = value (value is the frequencies for the word)
    Result = sorted(counter_dict.items(),key = lambda x: x[1], reverse = True)

    return Result

# 3 the function which calls the above 2 functions
def stats_text(text):

    # judge if the type of input is correct.
    if type(text)==str:
        pass
    else:
        raise ValueError('The input text is not the type of String')

    # for chinese words
    Result_cn = stats_text_cn(text)

    # for english words
    # remove of the chinese characters in the text
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            text = text.replace(character,'')
    # print("seeeeeeee no chinese okay",text)
    Result_en = stats_text_en(text) # text is non-chinese text

    Result = Result_cn + Result_en # list + list

    return Result



text1 = '''
Filled with admiration for Yugong, the Emperor of Heavens ordered
two mighty gods to carry the mountains away.
天神充满了对愚公的敬佩，命令幸运之神来把山给移开。
'''
text2 = ['a','b']


if __name__ == "__main__":
    # a example calling the function english text
    try:
        print('the sorted word frequencies for the input text1 \n',stats_text(text1))
        print('the sorted word frequencies for the input text2 \n',stats_text(text2))
    except Exception as e:
        print(e)