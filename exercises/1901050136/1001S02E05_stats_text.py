# this script is to implement the dictionary in which doing number counting of the words, 
# sort the words in the dict

text_sample = '''
Beautiful is better than ugly.
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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 2.1 counting the number of each word in the text
# eliminate the redundant symbols in the text 

text = text_sample.split()
# print(text)
symbols = '.,*-!' # the redundant symbols
words = []
for word in text:
    for symbol in symbols:
        word = word.replace(symbol,'')# word = 
    # if len(word):
    words.append(word)
print("\n",words)

# set in which there is no repetitive elements 
word_set = set(words)

# dictionary
counter_dict = {}
# tel['guido'] = 4127
for word in word_set:
    counter_dict[word] = words.count(word)
print("the frequency for each word in the set",counter_dict)

# sort the set in the sequence of the frequency descendingly
print("sort the set in the sequence of the frequency descendingly \n",
sorted(counter_dict.items(), key = lambda x: x[1],reverse = True)) # lambda 
# the items() of the dict will spit out (key, value), we use the key to sort, which is the x[1]

