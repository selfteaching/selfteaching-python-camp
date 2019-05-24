def stats_text(str):
    for char in str:
        if (char >= '\u4e00' and char <= '\u9fa5'):
            return stats_text_cn(str)
        else:
            return stats_text_en(str)
def stats_text_en(str): #定义该函数为用于统计text中各个英文单字出现的次数，并按词频降序排列
    str = str.lower() #将所有单词的字母转换成小写
    str = str.split() #将字符串转换为单词列表
    punc = ',.”?“!' #第11行-第14行为去掉文中的标点符号
    for i in punc:
        if i in str:
            str = str.replace(i, ' ')
    word = {} #第15行-第22行为统计各单词出现的次数
    for word1 in str:
        if word1 in word:
            count = word[word1]
        else:
            count = 0
        count = count + 1
        word[word1] = count
    return(sorted(word.items(), key = lambda e:e[1], reverse = True)) #将统计结果按次数的大小将序排列并输出结果
def stats_text_cn(str): #定义该函数为用于统计text中各个汉字出现的次数，并按词频降序排列
    str = str.split()
    str = str.strip()
    str = str.replace('\n', '') #去除换行符
    punc = '。，、「:?」' #第28行-第31行为去掉文中的标点符号
    for i in punc:
        if i in str:
            str = str.replace(i, '')
    pas = {} #第32行-第39行为统计各汉字出现的次数
    for char1 in str:
        if char1 in pas:
            count = pas[char1]
        else:
            count = 0
        count = count + 1
        pas[char1] = count
    return(sorted(pas.items(), key = lambda e:e[1], reverse = True)) #将统计的汉字的数量按降序排列并输出