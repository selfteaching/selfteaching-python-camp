# Filename : 1001S02E05_string.py
# author by : ÕÅ½ðÀÚ

text = '''
The Zen of Python, by Tim Peters
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
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

text_new = text.replace('better', 'worse')
print('better <--> worse:', '\n', text_new)


text_new_split = text_new.split()
temp = []
for i in text_new_split:
    if 'ea' in i:
        temp.append(i)
        
#print('the lengh of text_new_split:', len(text_new_split))

for i in range(len(temp)):
    text_new_split.remove(temp[i])
   
#print('the lengh of text_new_split:', len(text_new_split))

print('removed text:', '\n', text_new_split)
        
text_remove = " ".join(text_new_split)
text_A = text_remove.swapcase()
print('Reversed:', '\n', text_A)

text_A_split = text_A.split()
text_A_split.sort()
print('Sorted:', '\n', text_A_split)