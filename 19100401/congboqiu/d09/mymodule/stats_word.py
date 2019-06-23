
import re
from collections import Counter
counter=100
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



    


