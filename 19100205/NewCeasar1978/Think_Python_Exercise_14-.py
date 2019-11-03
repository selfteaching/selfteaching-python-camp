from mymodule.Think_Python_modules import anagram_sets
def store_anagrams(filename):
    dic = anagram_sets()
    fin = open(filename,'w')
    for word in dic:
        fin.write(word+':'+str(dic[word])+'\n')

def read_anagrams(filename,word):
    fr = open(filename)
    word_list = list(word)
    word_list.sort()
    signature = ''.join(word_list) + ':'
    for line in fr:
        if signature == line[:len(word)+1]:
            print(line)
            return

        

        
#store_anagrams('shelf.txt')
read_anagrams('shelf.txt','pussy')
    
