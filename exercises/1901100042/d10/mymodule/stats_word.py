from collections import Counter 
import jieba#引入jieba
#定义一个统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_en(text,count):
    #首先判断text类型，如果不是str，抛出ValueError
    if not isinstance(text,str):
        raise ValueError('输入的参数类型必须为str,当前参数类型为%s'%type(text))

    elements = text.split()
    words =[]
    symbols = ',.!*-?'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)

 
#定义一个统计参数中每个中文单词出现的次数，最后返回一个按词频降序排列的数组
def stats_text_cn(text,count):
    #同样先判断text类型
    if not isinstance(text,str):
        raise ValueError('输入的参数类型必须为str,当前参数类型为%s'%type(text))
    cn_elements = []
#中文直接指定unicode中的中文范围   英文是否可以同样进行指定Unicode范围操作？
#英文unicode对应的只有字母，没有单词，所以利用上述方法统计单词出现频数。
    cn_cut =jieba.cut(text,cut_all=False)
    for cn_element in cn_cut:
        if '\u4e00' <= cn_element <= '\u9fef' and len(cn_element)>=2:
            cn_elements.append(cn_element) 
    return Counter(cn_elements).most_common(count)

    
#输出合并词频统计
def stats_text(text,count):
    #同样先判断text类型
    if not isinstance(text,str):
        raise ValueError('输入的参数类型必须为str,当前参数类型为%s'%type(text))
    return stats_text_en(text,count)+stats_text_cn(text,count)


