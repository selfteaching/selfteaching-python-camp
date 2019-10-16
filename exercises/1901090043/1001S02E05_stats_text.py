import operator
import pprint
text = '''
The Zen of Python, by Tim Peters Beautiful is better than ugly.
Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.
Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.
Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
 '''
new_text = text.replace(',',' ')
new_text = new_text.replace('.',' ')
new_text = new_text.replace('!',' ')
new_text = new_text.replace('-',' ')
new_text= new_text.replace('*',' ')

#print(new_text)
new_text = new_text.split(' ')
d={}
for word in new_text:
    word = word.strip()
    if not word in d:
        if word != '':
            if word != "\n":
                d[word]=1
    else:
        d[word]=d[word]+1
 
new_text = sorted(d.items(),key = operator.itemgetter(1),reverse = True)

pprint.pprint(new_text)