# -*- coding: GBK -*-
import stats_word
text = stats_word.text
dict_order = stats_word.stats_text(text)
print(dict_order)
num = 0
for va in dict_order.values():
   #I am afraid  some charaters were lost, So I summary the number of the dictionary.
    num += va
print(num)
