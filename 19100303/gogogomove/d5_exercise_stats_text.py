text = '''The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!'''
k1=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')#将非英文字符替换为空格
k1=text.lower()
k1=text.split() # above all is to make it clean
dictionary={} # define a empty dic first
for i in k1: 
    count=k1.count(i)  # start counting the times each word appeared for
    r1={i:count}   # introduce a dictionary for continuously memo each word and times of its appearing??
    dictionary.update(r1) # as long as one memo generated above, update which as one key&value pair into the empty dic previously defined? 
print(dictionary)
# now to sort if from more to less times of words' appearing
# googled a expression called "lambda"- strange word for me anyway
sorted(dictionary.items(), lambda x: cmp(x[1]))  # tried times but alwasy show the erro:TypeError: sorted expected 1 arguments, got 2
