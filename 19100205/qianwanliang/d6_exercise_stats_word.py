text =  '''
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
相对论是关于时空和引力的理论，主要由爱因斯坦创立，依其研究对象的不同可分为狭义相对论和广义相对论。相对论和量子力学的提出给物理学带来了革命性的变化，它们共同奠定了现代物理学的基础。相对论极大地改变了人类对宇宙和自然的“常识性”观念，提出了“同时的相对性”、“四维时空”、“弯曲时空”等全新的概念。不过近年来，人们对于物理理论的分类有了一种新的认识——以其理论是否是决定论的来划分经典与非经典的物理学，即“非经典的=量子的”。在这个意义下，相对论仍然是一种经典的理论。
'''

import collections
import re

def stats_text_en(text_en):
    
    result = re.sub("[^A-Za-z]", " ", text_en.strip())
    newList = result.split( )
    
    for i in range(0,len(newList)):
        newList[i]=newList[i].strip('*-,.?!')
        if newList[i]==' ': 
            newList[i].remove(' ')
        else:
            i=i+1
    print('英文单词词频统计结果： ',collections.Counter(newList),'\n')


def stats_text_cn(text_cn):
  
    result1 = re.findall(u'[\u4e00-\u9fff]+',text_cn)
    newString = ''.join(result1)

    def stats(orgString, newDict) :
        d = newDict
        for m in orgString :
            d[m] = d.get(m, 0) + 1
        return d
    
    new_list = []
    for char in newString :
        cn = char.strip('-*、。，：？！……')
        new_list.append(cn)
    
    words = dict()
    for n in range(0,len(new_list)) :
        words = stats(new_list[n],words)
    newWords = sorted(words.items(), key=lambda item: item[1], reverse=True) 
    print('中文汉字字频统计结果： ',dict(newWords))

stats_text_en(text)
stats_text_cn(text)