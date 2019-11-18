def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型 %s' % type(text))
    elements = text.split()
    words = []
    symbols = ',.*_!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
   # print('正常的英文单词 ==>',words)

    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] = words.count(word)
    #print('英文单词出现的次数 ==>',counter)
    #print('从大到小输出所有的单词及出现的次数 ==>',sorted(counter.items(),key=lambda x: x[1],reverse=True))
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型 %s' % type(text))
    cn_characters = []
    for character in text:
        if '\u4e00'<= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set =set (cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

def stats_text(text):
    '''
    合并 英文词频 和 中文字频 的结果
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型 %s' % type(text))
    return stats_text_en(text) + stats_text_cn(text)

    

en_text='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

cn_text ='''
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
复杂胜于凌乱
可读性很重要
即便假借特例的实用性之名，也不可违背这些规则
不要包容所有错误，除非你确定需要这样做
做也许好过不做，但不假思索就动手还不如不做
。。。
'''


if __name__=='__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_en(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n',en_result)
    print('统计参数中每个中文单词出现的次数 ==>\n',cn_result)
