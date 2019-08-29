
# This algorithm uses dictionary to count and sort the word in the text
import re
import string
text = "The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to doit.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"

# Use re.split to split the string into list
text = re.split(r"(?:[\s!#$%&\*+,-./:;<=>?@^_`{|}~])",text)     #[] sperate the multiple symbol, \s serate the space, ?: exclude the symbol from the list
# Remove all the empty element in the list
while '' in text:
    text.remove('')

D={}    # Create empty dictionary
# Count the word use dictionary
for char in text:
    if char not in D:   # Set the word to 1 if the word not yet in dictionary
        D[char]=1
    else:       # The count plus 1 if the word already in dictionary
        D[char]+=1

# Sorted the dictionary by value in decreasing order

import re
text = "The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to doit.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
text = re.split(r"(?:[\s,.!*?-])",text)
while '' in text:
    text.remove('')

D={}
for char in text:
    if char not in D:
        D[char]=1
    else:
        D[char]=D[char]+1



D=sorted(D.items(),key=lambda D:D[1],reverse=True)

print(D)