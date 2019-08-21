
# This algorithm allowed us take any text input in string form, seperate them into single words and sorted by alphabet order
import re
text = "The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to doit.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"

# Use re.split to split the string into list
text = re.split(r"(?:[\s,.!*?-])",text)         #[] sperate the multiple symbol, \s serate the space, () exclude the symbol from the list
# Remove all the empty element in the list
while '' in text:
    text.remove('')

# Replace all the 'better' element by 'worse'

import re
text = "The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to doit.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
text = re.split(r"(?:[\s,.!*?-])",text)
while '' in text:
    text.remove('')

for i in range(0,len(text)):
    if text[i]=='better':
        text[i]='worse'


relist=[]       # Create a list to store the word include 'ea'
# Check all the element and store the element with 'ea' into the list
for i in range(0,len(text)):
    if 'ea' in text[i]:
        relist.append(text[i])
# Remove the element in the relist from the origin list

relist=[]
for i in range(0,len(text)):
    if 'ea' in text[i]:
        relist.append(text[i])

for rem in relist:
    while rem in text:
        text.remove(rem)


# Swap the uppercase and lowercase for each element 
for i in range(0,len(text)):
        text[i]=text[i].swapcase()

# Sort the list by alphabet order

for i in range(0,len(text)):
        text[i]=text[i].swapcase()
        

text.sort()

print(text)