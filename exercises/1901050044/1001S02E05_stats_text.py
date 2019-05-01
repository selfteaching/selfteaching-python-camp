 
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
punctuation = [',','.','--','*','!','?','\n']
for i in punctuation:
    text = text.replace(i," ") 
text = text.replace('\'re', ' are')
text = text.replace('aren\'t', ' are not')
text = text.replace('it\'s', 'it is')
text = text.replace('let\'s', 'let us')
list1 = text.split(' ')
for i in list1:
    if '' in list1:
        list1.remove('')
dictionary = {}
for word in list1:
    if not word in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word]+= 1
print(sorted(dictionary.items(), key = lambda item :item[1],reverse=True))