text = '''
The The Zen of The Python, by Tim Peters
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
print(text.replace("better","worse"))
text = text.replace("better","worse")                   #replace the "better" with "worse"
text = text.replace("--","")
text = text.replace(".","")
text = text.replace("!","")
text = text.replace(",","")
text = text.replace("*","")
list1 = text.split()
templist = []
#print(list1)
consquence = []

dictionary_1 = {}                               #use dictionanry to count the list1
for i in list1:
    if i in dictionary_1:
        dictionary_1[i] += 1
    else:
        dictionary_1[i] = 1
#print(dictionary_1)
templist = sorted(dictionary_1.items(), key=lambda d:d[1], reverse = True )     #sort the dictionary and output a list contains tuples
#print(templist)
dictionary_1 = {}                                                               #reset the dictionary
for i in templist:                                                              #change the list to sorted dictionary
    dictionary_1[i[0]] = i[1]

#sored_dic = sorted(dictionary_1.items())
print(dictionary_1)



