from collections import Counter

def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型,输入的类型 %s' %type(text))
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element =element.replace(symbol,'')
        if len(element):
           words.append(element)
    return Counter(words).most_common(count)

def stats_text_cn(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型,输入的类型 %s' %type(text))
    cn_characters=[]
    for character in text:
        if '\u4e00' <=character<='\u9fff':
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)


#if __name__== '_main_':
def stats_text(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型,输入的类型 %s' %type(text))
    en_result=stats_text_en(text,count)
    cn_result=stats_text_cn(text,count)
   #print('统计参数中每个英文单词出现的次数',en_result)
   #print('统计参数中每个中文汉字单词出现的次数',cn_result)

    return en_result + cn_result

   
