import re

def stats_text_en(text):
    #erros and Exception
    try:
        if not isinstance(text,str):
            raise ValueError(text)
    except ValueError as err:
            print('调用stats_text_en函数，参数类型错误:',type(err))


    # First changing "\n" into " ", 
    # then changing all charactor into lowercase
    # then removing non-english or no-space charactor
    text_p = text.replace("\n", " ").strip().lower()
    i = re.compile("[^a-zA-Z0-9 ]")
    text_en = i.sub("", text_p)

    # split, if has "" item , remove    
    text_to_list = text_en.split(" ")
    while "" in text_to_list:
        text_to_list.remove("")

    # create dictionary
    sort_list = [(x, text_to_list.count(x)) for x in set(text_to_list)]
    sort_dict = dict(sort_list)
    
    # output a dictionary sort by frequency
    return (sorted(sort_dict.items(), key=lambda x: x[1], reverse=True))


# 
def stats_text_cn(text):
     #erros and Exception
    try:
        if not isinstance(text,str):
            raise ValueError(text)
    except ValueError as err:
            print('调用stats_text_cn函数，参数类型错误:',type(err))
    # remove chinese symbol and "\n" and " " and, don't forget english and number charactor...
    i = re.compile("[ \,，\;；\.。：、\{\}\[\]「」\*—~\-\?？！\!‘\'’“\"”\nA-Za-z0-9]")
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



def stats_text(text):
     #erros and Exception
    try:
        if not isinstance(text,str):
            raise ValueError(text)
    except ValueError as err:
            print('调用stats_text函数，参数类型错误:',type(err))
    # Handling text 
    sort_en = stats_text_en(text)
    sort_cn = stats_text_cn(text)
    
    # print with a nicer neat
    i = 1
    print()
    print("Englise:", end="\n\n")
    for (x, y) in sort_en:
        while len(x) < 14:
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




    


