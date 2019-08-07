# This program is used to take english words or chinese words from a string. and make a 
# statistics. display the result with a descending order
#
#####################################
# -*- coding: uft-8 -*-
from collections import Counter
text ='''
寒來暑往，他們要⼀年才能往返渤海⼀次。
住在⿈河河畔的智叟，看⾒他們這樣⾟苦，取笑愚公說：「你不是很愚蠢嗎？你已⼀把年紀
了，就是⽤盡你的氣⼒，也不能挖去⼭的⼀⻆呢？」
愚公歎息道：「你有這樣的成⾒，是不會明⽩的。你⽐那寡婦的⼩兒⼦還不如呢！就算我死
了，還有我的兒⼦，我的孫⼦，我的曾孫⼦，他們⼀直傳下去。⽽這⼆⼭是不會加⼤的，總有
⼀天，我們會把它們剷平。」
智叟聽了，無話可說：
⼆⼭的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位⼤
⼒神揹⾛⼆⼭。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked
yugong’s way making it inconveni
'''

#split the string to list for statistic
def stats_text_en(text):
    # if text is not a string ,then raise a ValueError
    if type(text) != str:
        raise ValueError("you should give a string!")
            
    #counts the number of text, and return a list ordered by the consquences.
    list_en = text.split()
    words = []
    for j in list_en:
        word = ""
        for i in j:
            if (u'\u0041' <= i <=u'\u005a') or (u'\u0061' <= i <=u'\u007a'):
                word += i
                #delete all the chars which is not letters
        if word != "":
            words.append(word)
    #return result
       
    dictionary_1 = {} 
    set_word = set(words)
    #use the dictionary to make the order of the words
    #use dictionanry to count the list1                              
    for word in set_word:
        dictionary_1[word] = words.count(word)
    # get a dictionary with all the words
    templist = sorted(dictionary_1.items(), key=lambda d:d[1], reverse = True )     #sort the dictionary and output a list contains tuples
    # to order the dictionary descendingly
    dictionary_1 = {}                                                               #reset the dictionary
    for i in templist:                                                              #change the list to sorted dictionary
        dictionary_1[i[0]] = i[1]

    #sored_dic = sorted(dictionary_1.items())
    return dictionary_1
    #print(dictionary_1)

def stats_text_cn(text):
    # if text is not a string ,then raise a ValueError
    if type(text) != str:
        raise ValueError("you should give a string!")
    # this is the function of statistic the chinese words
    list_ch = []
    text_ch = ""
    for i in text:
        if u'\u4e00' <= i<=u'\u9fff':
            list_ch.append(i)
    set_words = set(list_ch)
    dic_ch = {}
    for word in set_words:
        dic_ch[word] = text_ch.count(word)
    list_ch = sorted(dic_ch.items(),key = lambda d:d[1],reverse = True)
    dictionary_1 = {}                                                               #reset the dictionary
    for i in list_ch:                                                              #change the list to sorted dictionary
        dictionary_1[i[0]] = i[1]
    return dictionary_1

def stats_text(text):
    # if text is not a string ,then raise a ValueError
    if type(text) != str:
        raise ValueError("you should give a string!")
    #call the two fuctions to statistic the word of a string
    result_en = stats_text_en(text)
    result_ch = stats_text_cn(text)
    result_en.update(result_ch)
    #merge the two dics to one
    print(Counter(result_en).most_common(30))
    '''
    list_all = sorted(result_en.items(),key = lambda d:d[1],reverse = True)
    dictionary_1 = {}                                                               #reset the dictionary
    #order the dictionary again
    for i in list_all:                                                              #change the list to sorted dictionary
        dictionary_1[i[0]] = i[1]
    return dictionary_1
    '''
if __name__ == '__main__':
    result_all = stats_text(text)
    print(result_all)
  #  text_ch = stats_text_cn(text)
  #  print(text_ch)






