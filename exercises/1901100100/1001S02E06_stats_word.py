# This program is used to take english words or chinese words from a string. and make a 
# statistics. display the result with a descending order
#
#####################################

text = '''
The The Zen of The Python, by Tim Peters
优美胜于丑陋
Beautiful is better than ugly.
明了胜于晦涩
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特例的实用性之名，也不可违背这些规则
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是 Python 之父
做也许好过不做，但不假思索就动手还不如不做
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然
命名空间是一种绝妙的理念，我们应当多加利用
'''

list_en = text.split()
#split the string to list for statistic
def stats_text_en(list_words):
    #counts the number of text, and return a list ordered by the consquences.
    words = []
    for j in list_words:
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
    # this is the function of statistic the chinese words
    list_ch = []
    text_ch = ""
    for i in text:
        if u'\u4e00' <= i<=u'\u9fff':
            text_ch += i
    for i in text_ch:
        list_ch.append(i)
    set_words = set(list_ch)
    dic_ch = {}
    for word in set_words:
        dic_ch[word] = text_ch.count(word)
    list_ch = sorted(dic_ch.items(),key = lambda d:d[1],reverse = True)
    #print(list_ch)
    return  list_ch


if __name__ == '__main__':
    result_en = stats_text_en(list_en)
    print(result_en)
    text_ch = stats_text_cn(text)
    print(text_ch)

    




