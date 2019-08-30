def stats_text_en(text):
    """
    返回按照单词词频顺序排序的数组。
    """
    text = text.replace('-','').replace('.','').replace('*','').replace('!','').replace(',','')

    word = text.split()
    wordDic = {}
    for key in word:
        if key in wordDic:
            wordDic[key] +=1
        else:
            wordDic[key] = 1


    #返回元素魏元组的列表
    wordSort = sorted(wordDic.items(),key = lambda x:x[1],reverse=True)
    #print(wordSort)
    print(dict(wordSort))
    return dict(wordSort)

def stats_text_cn(text):
    """
    统计中文词频。。。
    """
    text = text.replace('。','').replace(',','').strip()
#    print(text)
    word = text.split('，')

    word_s = "".join(word)
    word_dict = {}
    for a in word_s:
        if a not in word_dict:
            word_dict[a] =1
        else:
            word_dict[a] +=1
    
    #返回按降序排序的列表
    wordSort = sorted(word_dict.items(),key = lambda x:x[1],reverse=True)
    print(wordSort)





str1='''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
Namespaces are one honking great idea -- let's do more of those!'''

str2 ='''
学习了字符串相关操作，包括字符串转列表，字符串替换字符，删除字符串，大小写翻转，排序等。
'''


#stats_text_en(str1)
stats_text_cn(str2)
    