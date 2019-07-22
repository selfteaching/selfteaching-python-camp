def stats_text_en(text):
    from collections import Counter
    if not isinstance(text,str):
        raise TypeError('bad operand type')
    text = ascii(text)
    new_list = text.split(' ')
    new_list1 = []
    for i in new_list:
        new_list1.append(i.lower())
    print(Counter(new_list1))
def stats_text_cn(text):
    from collections import Counter
    if not isinstance(text,str):
        raise TypeError('bad operand type')
    new_list3 = []
    for i in text:
        new_list3.append(ord(i))
    new_list4 = []
    for i in new_list3:
        new_list4.append(chr(i))
    print(Counter(new_list4))

def stats_text(text):
    """
    Count the frequency of each element of an array for both Chinese and English
    : param text: the text to be counted
    """
    import re
    if not isinstance(text,str):
        raise TypeError('bad operand type')
    # Build a list contains Chinese characters only
    cn = []
    for i in text:
        if ord(i) > 255:
            cn.append(i)
    # Build a list contains English words only
    en = re.findall('[a-zA-Z0-9]+',text)
    return (stats_text_cn(cn),stats_text_en(en))
           
