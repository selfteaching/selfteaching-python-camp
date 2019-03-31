import re

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

text_cn = """
虽然大多数的语言既可被编译又可被解译，但大多数仅在一种情况下能够
良好运行。在一些编程系124324统中，程序——要经过几个阶段的编译，一般而言，
后阶段的编译往往fsdf更接~近机器语言。这种wsdfs常用的使用技巧最早在年代末用
于，编译程序先编译一个叫做“代码”的转换程序，然后再使用虚拟器转
行于机器上的真实代码。这种成功的技巧之后又用于和二进制码，
在很多时候，中间过渡的代码往往是解译，而不是编译的
"""

def stats_text_en(text):
    # change "\n" into " ", then change all charactor into lowercase
    # and remove symbol
    t = text.replace("\n", " ").strip().lower()
    i = re.compile("[\.\-\*\!\,\']")
    text_rm_symbol = i.sub("", t)

    # split, if has "" item , remove    
    text_to_list = text_rm_symbol.split(" ")
    while "" in text_to_list:
        text_to_list.remove("")

    # create dictionary
    sort_list = [(x, text_to_list.count(x)) for x in set(text_to_list)]
    sort_dict = dict(sort_list)
    
    # output a dictionary sort by frequency
    return (sorted(sort_dict.items(), key=lambda x: x[1], reverse=True))

print(stats_text_en(text_en))
# [('is', 10), ('better', 8), ('than', 8), ('the', 6), ('to', 5)..
print("\n\n")


def stats_text_cn(text):
    # remove chinese symbol and "\n" and " " and, don't forget english and number charactor...
    i = re.compile("[，；。—~ ？!‘’“”\nA-Za-z0-9]")
    text_rm_symbol = i.sub("", text)

    # split
    text_to_list = []
    for x in text_rm_symbol:
        text_to_list.append(x)
    while "" in text_to_list:
        text_to_list.remove("")

    # create dictionary
    sort_list = [(x, text_to_list.count(x)) for x in set(text_to_list)]
    sort_dict = dict(sort_list)
    
    # output a dictionary sort by frequency
    return (sorted(sort_dict.items(), key=lambda x: x[1], reverse=True))

print(stats_text_cn(text_cn))
print("\n\n")
# [('的', 9), ('译', 8), ('编', 7), ('用', 5), 
# ('一', 4), ('往', 4), ('程', 4), ('在', 4), (
# '码', 4), ('代', 4), ('序', 3), ('后', 3), ('
# 多', 3), ('种', 3), ('器', 3), ('言', 3)...


# addition
# It seems chinese can print with a nicer neat...
for x in stats_text_cn(text_cn):
    if (stats_text_cn(text_cn).index(x) + 1 )% 5 != 0:
        print(x, end=" ")
    else:
        print(x)
print("\n\n")

# ('的', 9) ('译', 8) ('编', 7) ('用', 5) ('码', 4)
# ('代', 4) ('一', 4) ('在', 4) ('程', 4) ('往', 4)
# ('器', 3) ('于', 3) ('种', 3) ('言', 3) ('后', 3)
# ......

# or ...

i = 1
for (x,y) in stats_text_cn(text_cn):
    if i % 5 != 0:
        print(x, ":", y, "|", end=" ")
    else:
        print(x,":", y, "|")

    i = i + 1
print()
# 的 : 9 | 译 : 8 | 编 : 7 | 用 : 5 | 代 : 4 |
# 码 : 4 | 程 : 4 | 往 : 4 | 一 : 4 | 在 : 4 |
# 后 : 3 | 器 : 3 | 序 : 3 | 多 : 3 | 种 : 3 |
# 于 : 3 | 言 : 3 | 段 : 2 | 过 : 2 | 又 : 2 |
