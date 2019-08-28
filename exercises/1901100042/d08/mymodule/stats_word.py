#定义一个统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_en(text):
    #首先判断text类型，如果不是str，抛出ValueError
    if not isinstance(text,str):
        raise ValueError('输入的参数类型必须为str,当前参数类型为%s'%type(text))
#以下内容摘自day5作业
    elements = text.split()
    words =[]
    counter = {}
    symbols = ',.!*-?'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    word_set =set(words)

#for word in words:
    for word in word_set:
        counter [word] = words.count(word)

 
#此处需用return返回函数值，如果没有return，返回值为None
    return sorted(counter.items(),key = lambda x:x[1],reverse = True)


#定义一个统计参数中每个中文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_cn(text):
    #同样先判断text类型
    if not isinstance(text,str):
        raise ValueError('输入的参数类型必须为str,当前参数类型为%s'%type(text))
    cn_elements = []
#中文直接指定unicode中的中文范围   英文是否可以同样进行指定Unicode范围操作？
#英文unicode对应的只有字母，没有单词，所以利用上述方法统计单词出现频数。
    for cn_element in text:
        if '\u4e00' <= cn_element <= '\u9fef':
            cn_elements.append(cn_element) 
    counter = {}
    cn_element_set = set(cn_elements)
    for element in cn_element_set:
        counter[element] = cn_elements.count(element)
    return sorted(counter.items(),key = lambda x:x[1],reverse = True)

    
#输出合并词频统计
def stats_text(text):
    #同样先判断text类型
    if not isinstance(text,str):
        raise ValueError('输入的参数类型必须为str,当前参数类型为%s'%type(text))
    return stats_text_en(text)+stats_text_cn(text)


if __name__ == '__main__':
    en_result = stats_text_en(text)
    print('统计参数中每个英文单词出现的次数==>',en_result)
    cn_result = stats_text_cn(text)
    print('统计参数中每个英文单词出现的次数==>',cn_result)