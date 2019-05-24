from collections import Counter

# 统计字符串中每个英文单词出现的次数，返回一个按词频降序排列的数组
def stats_text_en (text, n):

    if isinstance(text, str) == False:
        raise TypeError('Invalid type!')
    
    # 剔除字符串中的无意义字符
    s1 = text.replace('*', '', text.count('*'))
    s2 = s1.replace('-', '', text.count('-'))
    s3 = s2.replace(',', '', text.count(','))
    s4 = s3.replace('.', '', text.count('.'))
    s5 = s4.replace('“', '', text.count('“'))
    s6 = s5.replace('”', '', text.count('”'))
    s7 = s6.replace('’', '', text.count('’'))
    s8 = s7.replace('?', '', text.count('?'))
    text1 = s8.replace('!', '', text.count('!'))
    
    #拆分字符串为单词列表
    L = text1.split()

    #将单词列表转换以单词为key，以单词个数为value的字典
    i = 0
    aDict = {}

    while i < len(L) :
        cnt = text1.count(L[i])
        aDict.setdefault(L[i], cnt) 
        i = i + 1

    return(Counter(aDict).most_common(n))


# 统计字符串中每个中文汉字出现的次数，返回一个按字频降序排列的数组 
def stats_text_cn(text, n):

    if isinstance(text, str) == False:
        raise TypeError('Invalid type!')

    # 剔除字符串中的非中文字符
    s1 = text.replace('id', '', text.count('id'))
    s2 = s1.replace('contents', '', text.count('contents'))
    s3 = s2.replace('type', '', text.count('type'))
    s4 = s3.replace('author', '', text.count('author'))
    s5 = s4.replace('title', '', text.count('title'))
    s6 = s5.replace(',', '', text.count(','))
    s7 = s6.replace('\n', '', text.count('\n'))
    s8 = s7.replace('{', '', text.count('{'))
    s9 = s8.replace('}', '', text.count('}'))
    s10 = s9.replace('[', '', text.count('['))
    s11 = s10.replace(']', '', text.count(']'))
    s12 = s11.replace('！', '', text.count('！'))
    s13 = s12.replace('，', '', text.count('，'))
    s14 = s13.replace('。', '', text.count('。'))
    s15 = s14.replace('"', '', text.count('"'))
    s16 = s15.replace(':', '', text.count(':'))
    s17 = s16.replace('n', '', text.count('n'))
    s18 = s17.replace('\\', '', text.count('\\'))
    text1 = s18.replace(' ', '', text.count(' '))
    
    # 将字符串整理为以每个汉字为key，以该汉字个数为value的字典
    i = 0
    bDict = {}
    
    while i < len(text1):
        if text1[i] in range(1, 321):
            break
        else:
            cnt = text1.count(text1[i])
            bDict.setdefault(text1[i], cnt) 
            i = i + 1
    
    return(Counter(bDict).most_common(n))
