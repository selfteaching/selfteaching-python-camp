# 1.参考多位同学的优质代码，把自己代码变得更加简洁；
# 2.加入报错功能，在输入参数不是字符串的情况下提示；（有些地方还没考虑清楚，先加入一个最简单版本，再改进）
# 3.一些细节上的改进：
#     1）英文处理：因为英文很多时候有用“-”把多个单词连起来的习惯，所以在处理英文文本的时候，先把“-”换成空格；
#     2）排版改进：做了一点小调整，让英文的打印效果更好看
# ps.如果你在阅读，请别介意我那乱七八糟的英文，感谢有道~

import re

def stats_text_en(text):

    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    # first removing "-", useless space, then changing all words into lower-case.
    text_p = text.replace("\-", " ").strip().lower()
    # don't forget the "\n", Otherwise it will bring some awkawk words
    i = re.compile("[^a-z \n]")
    text_en = i.sub("", text_p).split()

    # create dictionary
    sort_list = [(x, text_en.count(x)) for x in set(text_en)]
    sort_dict = dict(sort_list)
    
    # output a dictionary sort by frequency
    return (sorted(sort_dict.items(), key=lambda x: x[1], reverse=True))


def stats_text_cn(text):

    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    # only chinese left and change into a list.
    list_cn = [i for i in text if u'\u4e00' <= i <= u'\u9fa5']

    # create dictionary
    sort_list = [(x, list_cn.count(x)) for x in set(list_cn)]
    sort_dict = dict(sort_list) 
    
    # output a dictionary sorted by frequency
    return (sorted(sort_dict.items(), key=lambda x: x[1], reverse=True))



def stats_text(text):
    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    sort_en = stats_text_en(text)
    sort_cn = stats_text_cn(text)


    # print with a nicer neat
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

    print("\n\n\n")
    print("Chinese:", end="\n\n")
    j = 1
    for (x,y) in sort_cn:
        if j % 6 != 0:
            print(x, ":", y, "|", end=" ")
        else:
            print(x,":", y)
        j = j + 1
    print()

