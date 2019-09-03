def stats_text_en (text):

    for i in range(len(text)):
        if (text[i] >= u'\u0041' and text[i]<=u'\u005a') or (text[i] >= u'\u0061' and text[i]<=u'\u007a'):
            break


    text_en = text[i:]
    text_en = text_en.replace('--', '')
    text_en = text_en.replace('!', '')
    text_en = text_en.replace('*', '')
    text_en = text_en.replace('.', ' ')
    text_en = text_en.replace(',', '')

    text_en = text_en.split()

    counter_en = collections.Counter(text_en)
    print("\n\nEN words frequency: ")
    print(counter_en)

    return counter_en




def stats_text_cn (text): 
    text_cn = ''

    for ch in text:
        if u'\u4e00' <= ch <= u'\u9fff': 
            text_cn = text_cn + ch


    # text = text.replace('：', '')
    # text = text.replace('，', '')
    # text = text.replace('\n', '')
    #text = text.replace('*', '')
    #print ('first char:')
    #print (text[0])

    text_split = []

    for i in range(len(text_cn)):
        text_split.append(text_cn[i])

    counter_cn = collections.Counter(text_split)
    print("CN wrods frequency: ")
    print(counter_cn)
    return counter_cn

def stats_text (text): 
    
    stats_text_cn (text)
    stats_text_en (text)
