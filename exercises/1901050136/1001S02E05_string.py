# this script is to implement the action of replacing words, delete words with special indicators, 
# case swaping and sorting with initial letters sequence

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
# print(text_sample)
# 1.2 replace better by worse
text = text_sample.replace('better','worse')
print('replace the better by worse \n',text)

# 1.3 delete the word including 'ea'
words = text.split()
# print(texts)
# print(len(texts))
filter = []
for word in words:
    if word.find('ea') < 0: # if cannot find 'ea', output -1.
        filter.append(word) # filter is also a list
print('the list including all words without "ea" \n',filter)

# 1.4 case conversion for all words in the list *filter*
swapcase_list = []
for word in filter:
    swapcase_list.append(word.swapcase())
print("case swaping for the list of filter \n",swapcase_list)

# 1.5 sort the words in the swapcase_list in the ascending sequence
sorted_list = sorted(swapcase_list)# sorted(list,reverse = true) true means desending sequence
print("sorting the words in the swapcase_list ascengdingly",sorted_list)

