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
Namespaces are one honking great idea -- let's do more of those!
'''
text1=text.replace('better','worse')
print(text1)


line_list = []
for line in text1.split(sep=("\n")):
    word_list = line.split(" ")
    for word in word_list[:]:
        if "ea" in word:
            word_list.remove(word)
    line_list.append(' '.join(word_list))    #wrong for me

text2 = '\n'.join(line_list)
print(text2)  

text3=text2.swapcase()
print(text3)

text4=sorted(text3)
print(text4)

