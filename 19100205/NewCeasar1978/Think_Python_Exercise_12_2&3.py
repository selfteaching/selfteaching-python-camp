def make_worddic(filename):
    dic = {}
    with open(filename) as fin:
        for line in fin:
            word = line.strip().lower()
            dic[word] = True
    return dic


def signature(word):
    list_word = list(word)
    list_word.sort()
    s = ''.join(list_word)
    return s

def anagrams(filename):
    dic_word = make_worddic(filename)
    dic_all = {}
    for word in dic_word:
        s = signature(word)
        dic_all.setdefault(s,[]).append(word)
    dic_anag = {}
    for word in dic_all:
        if len(dic_all[word]) > 1:
            dic_anag[word] = dic_all[word]
    return dic_anag

def has_metathesis_pair(word1,word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 2


d = anagrams('words.txt')
count = 0
for list1 in d.values():
    for word1 in list1:
        for word2 in list1:
            if word1 < word2 and has_metathesis_pair(word1,word2):
                count += 1
                print(word1,word2,count)


