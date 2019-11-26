str_text= '''
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
str_text=str_text.replace('*','')             
str_text=str_text.replace('-','')
str_text=str_text.replace('.','')
str_text=str_text.replace('!','')
#print(str_text)

s_list = str_text.split()
'''
s_set = set(s_list)
#print(s_set)
s_dict = {}
for s_item in s_set:
    s_dict.update({s_item:s_list.count(s_item)})
print(sorted(s_dict.items(),key=lambda x:x[1],reverse=True))
'''
print('单词个数',len(s_list))