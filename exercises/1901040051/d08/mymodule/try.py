en_text = '''
The Zen of python,by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Comples is better than complicated.
Flat is better than dense.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it may be a good idea.
If the implementation is easy to explain,it may be a good idea.
Namespaces are one honking great idea--let's do more of those!
The Zen of python,by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Comples is better than complicated.
Flat is better than dense.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it may be a good idea.
If the implementation is easy to explain,it may be a good idea.
Namespaces are one honking great idea--let's do more of those!

'''


# def stats_text_en(en_text):

#     elements = en_text.split()

#     words = []

#     symbols = ',.*-!'

#     for element in elements:

#         for symbol in symbols:

#             element = element.replace(symbol,'')

#         if len(element)and element.isascii():

#             words.append(element)

#     counter = {}

#     word_set = set(words)



#     for word in word_set:

#         counter[word] = words.count(word)



#     return sorted(counter.items(), key=lambda x: x[1], reverse=True)

    





cn_text =  '''
轻轻的我走了
正如我轻轻的来
我轻轻的招手
作别西天的云彩
那河畔的金柳
是夕阳中的新娘
波光里的艳影
在我的心头荡漾
软泥上的青荇
油油的在水底招摇
在康河的柔波里
我甘心做一条水草
那榆荫下的一潭
不是清泉 是天上虹
揉碎在浮藻间
沉淀着彩虹似的梦
寻梦 撑一支长蒿
向青草更青处漫溯
满载一船星辉
在星辉斑斓里放歌
但我不能放歌
悄悄是别离的笙箫
夏虫也为我沉默
沉默是今晚的康桥
悄悄的我走了
正如我悄悄的来
我挥一挥衣袖
不带走一片云彩
'''

import re    #引入正则表达式，以便操作字符串

import collections   #引入collections模块，以便使用计数功能

# tt = re.sub('\n+', '\n',  cn_text) 
# print(tt)

def stats_text_en(en_text):

    if type(en_text)!= str:

        raise ValueError('文本为非字符串')

    en_text = re.sub("[^A-Za-z]", " ", en_text)

    en_text = en_text.lower()

    en_text = en_text.split()

    en_text = collections.Counter(en_text)

    print('英文单词词频: \n',en_text)



def stats_text_cn(cn_text):

    if type(cn_text) != str:

        raise ValueError('文本为非字符串')

    cn_text = re.sub("[A-Za-z.。，,'!！“”「」？?、：\"\-* \n]", "", cn_text)

    for t1 in cn_text:

        t1 = cn_text.split() 

    cn_text=collections.Counter(cn_text)         

    print('中文汉字字频：\n',cn_text)

stats_text_en(en_text)
stats_text_cn(cn_text)