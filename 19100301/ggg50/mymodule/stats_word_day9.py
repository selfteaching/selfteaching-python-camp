# day 9 改进：
# 1.调用 collections 这个标准库里面的 Counter object，相比之下更清晰易懂些；
# 2.把中英文两个打印功能，分别封装到对应的函数里面，这样的话，在外部无论是想单独统计中文、英文或者两者都统计，都会生成对应的文本打印。
# 也就是说，调用 stats_text_en 就是统计并打印英文，调用 stats_text 就是中英文都统计并打印；
# 3.我看到有写同学把读取“tang300.json”放在这个文件，我觉得更应该发在 main.py中，因为从思路是看，应该是我们在 main.py 获得一个文本，然后调用这个 module 里面的函数来统计和打印

import re
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

    # only chinese left and change into a list.
    list_cn = [i for i in text if u'\u4e00' <= i <= u'\u9fa5']
    
    # using Sounter to create a dictionary sorted by frequency
    sort_cn = Counter(list_cn).most_common(counter)

    # printing chinese
    print("Chinese:", end="\n\n")
    j = 1
    for (x,y) in sort_cn:
        if j % 6 != 0:
            print(x, ":", y, "|", end=" ")
        else:
            print(x,":", y)
        j = j + 1
    print()

    return sort_cn



def stats_text(text, counter):
    if not isinstance(text, str):
        raise ValueError("I can only handle a string type text")

    sort_en = stats_text_en(text, counter)
    sort_cn = stats_text_cn(text, counter)




