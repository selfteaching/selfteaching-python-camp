from collections import Counter
import re
import jieba


def stats_text_en(text, num):
    '''统计英文参数中的词频并且并且降序排列'''
    count = int(num)
    if type(text)is not str:
        raise ValueError("This value is\' string.")
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z]")  # 匹配不是中文、大小写 的其他字符
    text = cop.sub(' ', text)  # 将text中匹配到的字符替换成空字符
    list1 = text.split()
    list2 = []
    for i in list1:
        for uchar in i:
            if (uchar >= u'\u0041' and uchar <= u'\u005A') or (uchar >= u'\u0061' and uchar <= u'\u007A'):
                pass
            else:
                break
        else:
            list2.append(i)
    new_li = Counter(list2).most_common(count)
    return new_li



def stats_text_cn(text, num):
    '''统计中文参数中的词频并且并且降序排列'''
    count = int(num)
    if type(text)is not str:
        raise ValueError("This value is\' string.")

    list1 = []
    for i in text:
        if '\u4e00' <= i <= '\u9fff':
            list1.append(i)
    new_string = ''.join(list1)
    list3 = jieba.cut(new_string)
    list4 = []
    for i in list3:
        if len(i) >=2:
            list4.append(i)

    new_li = Counter(list4).most_common(count)
    return new_li



def stats_text(text, num):
    '''分别统计中文与英文词频并且合并输出'''
    li = []
    li.append(stats_text_en(text, num))
    li.append(stats_text_cn(text, num))
    return li


