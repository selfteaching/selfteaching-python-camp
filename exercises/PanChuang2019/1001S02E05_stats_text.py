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
elements=text.split()
word_amount=[]
symbols="*.-,!"
for element in elements:
    for symbol in symbols:
        element=element.replace(symbol,'')
    if len(element):
        word_amount.append(element)
print(word_amount)

counter={}
word_amount_set=set(word_amount)

for word in word_amount_set:
    counter[word]=word_amount.count(word)
print(counter)
print("这个是什么东东\n",counter.items())
print("排序\n",sorted(counter.items(),key=lambda x:x[1],reverse=True))
