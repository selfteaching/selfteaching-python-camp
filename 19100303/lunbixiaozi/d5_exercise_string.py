

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
#1.2
text = text.replace("better", "worse")
print('1.2: \n')
print(text)

#1.3
while ("ea" in text):
    index_ea=text.find('ea')
    index_start=index_ea-1
    index_end=index_ea+2
    while((text[index_start] != " ") and (text[index_start] != '\n') and (text[index_start] != '.')):
        index_start = index_start-1
    while((text[index_end] != " ") and (text[index_end] != '\n') and (text[index_end] != '.')):
        index_end = index_end + 1
    text = text[:index_start+1]+text[index_end:]
print('1.3: \n')
print (text)

#1.4
new_text = ''
for i in range(len(text)):
    if text[i].isupper():
        new_text = new_text + text[i].lower()
    elif text[i].islower():
        new_text = new_text + text[i].upper()
    else:
        new_text = new_text + text[i]

text=new_text
print('1.4: \n')
print (text)

#1.5
text = text.replace('-', ' ')
text = text.replace('.', ' ')
text = text.replace('\n', ' ')
text = text.replace('*', ' ')   
words=text.split()
words.sort()
print('1.5: \n')
print(words)




