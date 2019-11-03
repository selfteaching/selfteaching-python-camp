from mymodule.Think_Python_modules import make_worddic
word_all = make_worddic('words.txt')

def children(word):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_all:
            res.append(child)
    return res

def children_list(word_list):
    res = []
    for word in word_list:
        res += children(word)
    return res

def is_reducible(word_list):
    if 'a' in word_list or 'i' in word_list:
        return True
    elif word_list == []:
        return False
    else:
        return is_reducible(children_list(word_list))

longest_word = ''
n = 1
for word in word_all:
    if ('a' in word or  'i' in word) and len(word) > n and is_reducible([word]):
        n = len(word)
        longest_word = word   
for word in word_all:
    if ('a' in word or  'i' in word) and len(word) == n and is_reducible([word]):
        print(n,word)

'''#用非递归方式实现 is_reducible(word_list)
def is_reducible(word_list):    
    for i in range(len(word_list[0])-1):
        word_list = children_list(word_list)
    return word_list != []
'''



