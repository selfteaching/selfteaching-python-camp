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

text_a=text.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ').replace('.',' ')
text_b=text_a.lower()
text_c=text_b.split()
word_dic={}
for i in text_c:
   count=text.count(i)
   text_count={i:count}
   word_dic.update(text_count)
print(word_dic)


word_dic1=sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
print(word_dic1)

