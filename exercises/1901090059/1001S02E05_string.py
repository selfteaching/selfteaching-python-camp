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

textBetterRepWorse = text.replace('better', 'worse')
#print(textBetterRepWorse)

textRemoveWordsInea = textBetterRepWorse.split()
textRemoveWordsIneaS = textBetterRepWorse
for a in textRemoveWordsInea:
    if 'ea' in a:
        a = a.rstrip('.')
      #  print(a)
        textRemoveWordsIneaS = textRemoveWordsIneaS.replace(a, '')
#print(textRemoveWordsIneaS)

RevertextRemoveWordsIneaS = textRemoveWordsIneaS.swapcase()
#print(RevertextRemoveWordsIneaS)

SortRevertextRemoveWordsIneaS = RevertextRemoveWordsIneaS.split()
SortRevertextRemoveWordsIneaS.sort()
#print(SortRevertextRemoveWordsIneaS)




