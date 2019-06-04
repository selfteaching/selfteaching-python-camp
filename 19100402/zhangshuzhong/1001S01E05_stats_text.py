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
#除去样本中的所有标点符号
symbol = ",.!-*"
for str in symbol:
    text= text.replace(str,'')
#将样本中的所有单词转换为小写
text=text.lower()

#将字符串转换成单词列表
text=text.split()
#创建一个空的字典
char_dict={}

#向字典中添加元素，主要的思路就是，将列表中的单词逐个与字典中的已有单词对比
#如果字典中有这个单词，那么这个单词个数就加1，如果没有这个单词就将这个单词添加到字典并将其单词个数加1。
for char1 in text:#从单词列表中逐个提取单词
    if char1 in char_dict:#将提取的单词与字典中的单词进行对比判断
        count=char_dict[char1]#如果字典中有那个单词，那么得出字典中单词已有的个数
    else:
        count=0#如果没有，那么这个单词现有的个数就为0
    count +=1#将这个单词的个数加1
    char_dict[char1]=count#向字典中重新添加单词个数,并开始下一个单词
    
    
print(char_dict)
    
char1_dict=sorted(char_dict.items(),key=lambda x:x[1],reverse=True)
#首先这里需要排序，那么我们需要调用sorted()函数
#需要排序的内容是字典中的单词以及词频，在这里将其当做一个元祖，及使用了items()函数，将字典中的数据生成为元祖来比较
#这里具体需要比较的是词频，所以这里使用了lambda函数，“lambda x:x[1]”中x表示一个元祖，x[1]表示将元祖中的第二个元素来比较
#sorted()函数默认的是顺序排列，所以这里讲为了实现倒序排列所以使用了reverse参数
print(char1_dict)
