import re
text_cn = """
好好学习，天天向上。1234567，pony
"""
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

print(dict(stats_text_cn(text_cn)))