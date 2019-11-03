import string
import collections
from mymodule.Think_Python_modules import make_worddic
from mymodule.Think_Python_modules import make_wordlist
word_dic = make_worddic('words.txt')
word_list_clear = make_wordlist('158-0.txt')
number = len(set(word_list_clear))
res = collections.Counter(word_list_clear).most_common(20)
diff = []
diff_num = 0
for word in word_list_clear:
    if word not in word_dic:
        diff.append(word)
        diff_num += 1
print(res)
print(number)
print(diff_num)
#print(diff)

