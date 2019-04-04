
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
In the face of ambxiguity,refuse the temptation to guess.
There should be one --and preferably only one --obvious way to do it.
Althoug that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let't do more of those!
'''

replacedText = text.replace("better", "worse")
#print(replacedText)

splitReplacedText = replacedText.split()
removedEaText = []
for i in splitReplacedText:
     letters=range(ord('A'),ord('Z')):
     if ord(i[0]) not in range(ord('A'),ord('Z')):
          print("Not a word:%s"%(i))
          
     if ord(i[lent(i)-1]) not in range(ord('A'),ord('Z')):
          print("Has dangle:%s"%(i))
          i.strip(i[len(i)-1])
          print("no dangle：%s"%(i))
          
