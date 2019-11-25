def stats_text_en(text):
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
    counter={}
    word_set=set(words)
    for word in word_set:
       counter[word] =words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型,输入的类型 %s' %type(text))
    cn_characters=[]
    for character in text:
        if '\u4e00' <=character<='\u9fff':
            cn_characters.append(character)
    counter={}
    cn_characters_set=set(cn_characters)
    for character in cn_characters_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


#if __name__== '_main_':
def stats_text(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型,输入的类型 %s' %type(text))
    en_result=stats_text_en(text)
    cn_result=stats_text_cn(text)
   #print('统计参数中每个英文单词出现的次数',en_result)
   #print('统计参数中每个中文汉字单词出现的次数',cn_result)

    return en_result + cn_result

   
