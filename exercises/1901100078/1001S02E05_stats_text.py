text='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
'''

def words_count(Str):
    #convert string to list
    words_list = Str.split()
    #remove the punctuation
    no_pun_list = []
    for word in words_list:
        word = word.strip('.!--*')
        #remove the number
        if word.isalpha():
            no_pun_list.append(word)
    #count the words in list
    words_dict = {}
    for word in no_pun_list:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    #print out as the sequence
    words_seq = sorted(words_dict.items(), key = lambda x: x[1], reverse = True)
    return words_seq


words_count(text)


