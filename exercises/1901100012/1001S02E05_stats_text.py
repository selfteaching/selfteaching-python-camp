text='''
The Zen of Python,by Tim Peters


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
In the face of ambxiquity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Altough that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it's a bad idea.
If the implementation is easy to explain,it's a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
 
eles=text.split()#将文章按照空格划分开 
words=[]
sys=".,-,*,!"
for elet in eles:
    for s1 in sys:
        elet=elet.replace(s1,' ')
    if len(elet):
        words.append(elet)
print(words)
print()

counter={}
word_set=set(words)
for word in word_set:
    counter[word]=words.count(word)
print(counter)
print()

print(sorted(counter.items(),key=lambda x:(x[1],x[0]),reverse=True))
