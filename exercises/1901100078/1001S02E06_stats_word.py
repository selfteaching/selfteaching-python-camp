def stats_text_en(text):
    ''' count the word in the text '''
    #convert string to list
    words_list = text.split()
    #remove the punctuation
    no_pun_list = []
    for word in words_list:
        word = word.strip('.!--*')
        #remove the number
        if word.isalpha():
            no_pun_list.append(word)
    #count the words in list
    words_dict = {}
    word_set = set(no_pun_list)
    for word in word_set:
        words_dict[word] = no_pun_list.count(word)
    #print out as the sequence
    words_seq = sorted(words_dict.items(), key = lambda x: x[1], reverse = True)
    return words_seq

import string
def stats_text_cn(text):
    '''统计中文字频'''
    List = [i for i in text]

    word_dict = {}
    for word in set(List):
        word_dict[word] = List.count(word)
    word_seq = sorted(word_dict.items(), key = lambda x: x[1], reverse = True)
    return word_seq

text = '离离原上草，春风吹又生！'
print(stats_text_cn(text))