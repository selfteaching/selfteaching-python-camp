#定义一个统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_en(text):
#以下内容摘自day5作业
    elements = text.split()
    words =[]
    counter = {}
    symbols = ',.!*-?'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element):
            words.append(element)
    word_set =set(words)

#for word in words:
    for word in word_set:
        counter [word] = words.count(word)

 
#此处需用return返回函数值，如果没有return，返回值为None
    return sorted(counter.items(),key = lambda x:x[1],reverse = True)


#定义一个统计参数中每个中文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_cn(text):
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

    

en_text = '''
this is a test?
is a test!
a test,
test.
t*
'''



cn_text = '''
这是一个测试，
是一个测试.
一个测试。
个测试？
测试?
试'''


if __name__ == '__main__':
    en_result = stats_text_en(en_text)
    print('统计参数中每个英文单词出现的次数==>',en_result)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数==>',cn_result)