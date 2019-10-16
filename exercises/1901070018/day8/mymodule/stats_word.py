def stats_text_en(text):
    '''统计英文参数中的词频并且并且降序排列'''
    if type(text)is not str:
        raise ValueError("This value is\' string.")
    char = ',.-:;!@#$%^&*()-+=<>?/\\`~|[]{}，。？、·~！@#￥%……&*（）——+-={}【】、|；：“”‘’'
    for i in char:
        text = text.replace(i, '')
    list1 = text.split()
    dic = {}
    list2 = []
    for i in list1:
        for j in i:
            if (65<=ord(j)<=90)or(97<=ord(j)<=122):
                list2.append(i)

    for i in list2:
        num = list2.count(i)
        dic[i] = num
    list3 = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    return list3


def stats_text_cn(text):
    '''统计中文参数中的词频并且并且降序排列'''
    if type(text)is not str:
        raise ValueError("This value is\' string.")
    list1 = []
    dic = {}
    for i in text:
        if '\u4e00' <= i <= '\u9fff':
            list1.append(i)
            dic[i] = list1.count(i)
    list2 = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    return list2

def stats_text(text):
    '''分别统计中文与英文词频并且合并输出'''
    li = []
    li.append(stats_text_en(text))
    li.append(stats_text_cn(text))
    return li


