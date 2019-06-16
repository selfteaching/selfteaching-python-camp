
# 统计字符串中每个英文单词出现的次数，返回一个按词频降序排列的数组
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

    while i < len(L) :
        cnt = text1.count(L[i])
        aDict.setdefault(L[i], cnt) 
        i = i + 1

    # 将字典中的单词按个数从大到小排序
    L1 = sorted(aDict.items(), key=lambda x: x[1], reverse=True)
    return L1

# 统计字符串中每个中文汉字出现的次数，返回一个按字频降序排列的数组 
def stats_text_cn(text):
    # 剔除字符串中的非中文字符
    s1 = text.replace('，', '', text.count('，'))
    s2 = s1.replace('“', '', text.count('“'))
    s3 = s2.replace('”', '', text.count('”'))
    s4 = s3.replace('——', '', text.count('——'))
    s5 = s4.replace('。', '', text.count('。'))
    s6 = s5.replace('……', '', text.count('……'))
    s7 = s6.replace(' ', '', text.count(' '))
    s8 = s7.replace('\n', '', text.count('\n'))
    text1 = s8.replace('？', '', text.count('？'))

    # 将字符串整理为以每个汉字为key，以该汉字个数为value的字典
    i = 0
    bDict = {}
    
    while i < len(text1):
        cnt = text1.count(text1[i])
        bDict.setdefault(text1[i], cnt) 
        i = i + 1
    
    # 将字典中的中文汉字按个数从大到小排序
    L2 = sorted(bDict.items(), key=lambda x: x[1], reverse=True)
    return L2


text_en = '''
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
print(stats_text_en(text_en))

text_cn = '''
有些概念，在绝大多数人脑子里干脆就是混沌的，比如“价值” —— 什么是价值？
如何衡量价值？“价值”这个概念，被我私下里称为“哈姆雷特概念”，
因为莎士比亚说，“一千个人眼里有一千个哈姆雷特”……一旦争论中出现这种概念上的冲突，
那么基本上争论演变成争吵，甚至只剩下吵，就是永恒的狗血结局。
'''

# 打印出排序后的汉字数组
print()
print(stats_text_cn(text_cn))