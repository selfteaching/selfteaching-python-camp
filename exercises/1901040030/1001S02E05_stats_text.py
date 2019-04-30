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
#先转换成列表
text_list=text.replace('.','').replace('--','').replace('*','').replace('!','').split()
#定义一个字典，遍历列表，如果列表的元素在字典的key里面，key的value+1，不在key里，key的value=1
text_dict={}
for word in text_list:
    if word in text_dict.keys():
        text_dict[word]=text_dict[word]+1
    else:
        text_dict[word]=1
#将字典的items已元祖的形式转换成列表，进行排序
text_list2=sorted(text_dict.items(),key=lambda item:item[1],reverse=True)
#输入列表里的每一项
for i in text_list2:
    print(i[0],":",i[1])


