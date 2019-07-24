def stats_text_en(text):
    text1=text.replace(',','').replace('.','').replace('*','').replace('!','').replace('--','')
    text2=text1.split()
    words=set(text2)
    d={}
    for word in words:                          #用word集合遍历每个不重复的单词
        c=text2.count(word)                     #用列表的count方法可得到列表内每个元素存在的个数
        d[word]=c                               #键为word，个数为值增添到字典
    s=sorted(d.items(),key=lambda d:d[1],reverse=True)       #用sorted方法可以快速对字典进行排序，其中key=lambda d:d[1]的0为键，1为值，最后返回一个列表
    list_key=[x[0] for x in s]                  #遍历排序后的列表，因列表的元素为元组，因此用x[0]获取元组指定下标的元素，最后得到该元素的列表
    return list_key


def stats_text_cn(text):
    words= [i for i in text if '\u4e00' <= i <= '\u9fa5']         #中文的Unicode编码范围为：[\u4e00-\u9fa5]，由此可获得字符串中的汉字列表   
    word_set=set(words)                                           #把汉字列表转换为集合去重，
    d={}
    for w in word_set:                                            #遍历汉字结合，用count方法可以直接判断出每个汉字在字符串中存在的个数
        c=words.count(w)
        d[w]=c                                                    #以汉字为键，个数c为值添加到字典d中
    list_word=sorted(d.items(),key=lambda d:d[1],reverse=True)    #对字典以键排序，获得排序后的列表，元素为键值对组成的元组
    return [i[0] for i in list_word]                              #返回每个元组的第一个元素，即原字典的键
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
s='努力，加油！冲鸭,鸭，snitt'
print(stats_text_en(text))
print('----------------按汉字个数降序输出------------------------')
print(stats_text_cn(s))