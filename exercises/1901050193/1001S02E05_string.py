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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those
'''
#1.1 Replace better with worse.
text = text.replace('better','worse')
print('1.1 Replace better with worse.',end='\n')
print(text)

#1.2 Delete words with 'ea'.
words=text.split()
str1=[]
for word in words:
    if word.find('ea')<0:
        str1.append(word)
print('1.2 Delete words with ea.', end='\n')
print(str1)

#1.3 Swap the capital letters and the small letters
swap=[i.swapcase()for i in str1]
print('1.3 Swap the capital letters and the small letters.',end='\n')
print(swap)

#1.4 Sort from a to z
print('1.4 Sort from a to z.',end='\n')
print(sorted(swap))