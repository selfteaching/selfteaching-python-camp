# day 10
# 1.今日安装并使用 jieba 第三方库，这个库专门用于中文文本的分词，

# 2.需要注意的是，jieba 在分词的时候，也会帮我们把英文单词找出来，所以在运用的时候，
#   还是需要提前把英文单词过滤掉；
#   另外，中文符号会留下，不过因为我们要找的是长度大于等于2的词，所以可以不用管了，
#   更进一步，也不应该管，因为中文的组词特点，直接把符号去掉可能会产生多余的词组
#   所以我的想法是，把符号保留，并且把英文都替换成“，”


import re
import jieba
from collections import Counter

def stats_text_en(text, counter):

    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    # first removing "-", useless space, then changing all words into lower-case.
    text_p = text.replace("\-", " ").strip().lower()
    # don't forgeting the "\n", Otherwise it will bring some awkawk words
    i = re.compile("[^a-z \n]")
    text_en = i.sub("", text_p).split()
    
    # using Sounter to create a dictionary sorted by frequency
    sort_en = Counter(text_en).most_common(counter)

    # printing english
    i = 1
    print()
    print("Englise:", end="\n\n")
    for (x, y) in sort_en:
        while len(x) < 15 - len(str(y)):
            x = x + " "
        if i % 3 != 0:
            print(x, y, "|", end=" ")
        else:
            print(x, y)     
        i = i + 1
    
    return sort_en


def stats_text_cn(text, counter):

    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    # only chinese left and changed into a list.
    text_cn = ""
    for t in text:
        if ord(t) > 256:
            text_cn = text_cn + t
        else:
            text_cn = text_cn + "，"
    list_cn_word = ([x for x in jieba.cut(text_cn, cut_all=False) if len(x) >= 2])

    # using Sounter to create a dictionary sorted by frequency
    sort_cn = Counter(list_cn_word).most_common(counter)

    # printing chinese
    i = 1
    print("Chinese:", end="\n\n")
    for (x, y) in sort_cn:
        x = x + (10 - len(x) * 2 - len(str(y))) * " "
        if i % 4 != 0:
            print(x, y, "|", end=" ")
        else:
            print(x, y)     
        i = i + 1
    print()

    return sort_cn



def stats_text(text, counter):
    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    sort_en = stats_text_en(text, counter)
    sort_cn = stats_text_cn(text, counter)




