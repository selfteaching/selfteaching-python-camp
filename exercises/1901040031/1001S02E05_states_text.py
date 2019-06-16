text = '''
The Zen of python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases arent't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced
In the face of ambxiguity,refuse the temptation to guess
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch
If the implementation is hard to explain,it's a bad idea
If the implementation is easy to explain,it's may be a good idea.
Namespaces are one honking great idea --let's do more of those!
'''
text = text.replace(',',' ').replace('.',' ').replace('--','').replace('!','').replace('*',' ').replace('\n','')
#将文本中的非英文字符替换为空格
text = text.lower()#全改为小写字母
text = text.split(' ')#切分为独立的词，以空格隔开

dict ={}#创建一个空的字典
for i in text:
    count = text.count(i)#对text文本中提取出的单词计数
    r1 ={i:count}
    dict.update(r1)#添加字典
print(dict)

dict1=sorted(dict.items(),key=lambda x:x[1],reverse=True)#按频次从大到小排序
print(dict1)