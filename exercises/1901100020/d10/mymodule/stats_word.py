from collections import Counter
import jieba
#<<<<<<< 1001S02E02_hello_python.py
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jieba
#=======

#>>>>>>> master
# 统计参数中每个英文单词出现的次数
def stats_text_en(text, count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        # 用str类型的isascii方法判断是否是英文单词
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)

# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text, count):
#<<<<<<< 1001S02E02_hello_python.py
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)
#=======
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)
#>>>>>>> master

def stats_text(text, count):
    '''
    合并 英文词频 和中文字频 的结果
    '''
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型，输入类型%s' % type(text))
    return stats_text_en(text, count) + stats_text_cn(text, count)