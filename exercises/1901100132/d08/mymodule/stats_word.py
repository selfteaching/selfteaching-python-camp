# 统计参数中英文单词出现的次数
def stats_text_en(text):
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型, 输入类型 %s' % type(text))
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        if len(element) and element.isascii():
                words.append(element)
    counter = {}
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

#统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型, 输入类型 %s' % type(text))
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

        
en_text = '''
The Zen of Python , by Tim Peters

Beautiful is better than ugly.
Explicit is better than implcit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases are't special enough to break the rules.
Although practicality beats purity.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one --- and preferably only one -- obvious way to do it.
Although the way may not be obvious at first unless you are a Dutch.
Now is better than never.
Although never is better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's maybe a good idea.
Namespaces are one honking great idea --- let's do more of those!
'''

cn_text = '''
Python 之禅 by Tim Peters

优美胜于丑陋
明了胜于晦涩
简介胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特例的实用性之名，也不可违背这些规则
不要包含所有错误，除非你确定需要这样做
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是Python 之父
做也许好过不做，但不假思索就动手还不如不做 
'''

def stats_text(text):
    #合并英文词频和中文词频
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型, 输入类型 %s' % type(text))
    return stats_text_cn(text) + stats_text_en(text)

if __name__ == '__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n', en_result) 
    print('统计参数中每个中文汉字出现的次数 ==>\n', cn_result)

