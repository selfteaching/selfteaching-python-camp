

def stats_text_en (text):
    # 剔除字符串中的无意义字符
    s1 = text.replace('*', '', text.count('*'))
    s2 = s1.replace('-', '', text.count('-'))
    s3 = s2.replace(',', '', text.count(','))
    s4 = s3.replace('.', '', text.count('.'))
    text1 = s4.replace('!', '', text.count('!'))

    #拆分字符串为单词列表
    L = text1.split()

    #将单词列表转换以单词为key，以单词个数为value的字典
    i = 0
    aDict = {}

    while(i < len(L)):
        cnt = text1.count(L[i])
        aDict.setdefault(L[i], cnt) 
        i = i + 1

    # 将字典中的单词按个数从大到小排序
    L1 = sorted(aDict.items(), key=lambda x: x[1], reverse=True)
    return(L1)


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

# 打印出排序后的单词数组
print(stats_text_en(text))