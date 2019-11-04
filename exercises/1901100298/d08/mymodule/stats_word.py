# 统计参数中每个英文单词出现的次数
def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'% type(text))
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element)and element.isascii():
            words.append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] =  words.count(word)
    # 函数返回值用 return 进行返回，如果没有 return 返回值则为none
    return sorted(counter.items(),key = lambda x:x[1],reverse = True)


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'% type(text))
    cn_characters = []
    for character in text:
        # unicode 中 中文字符的范围
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key = lambda x:x[1],reverse = True)


def stats_text(text):
    '''
    合并 英文词频 和 中文词频 的结果
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'% type(text))
    return stats_text_en(text) + stats_text_cn(text)
    

en_text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

cn_text = '''
美比丑好，明比涩强。
简胜于繁，繁强于难。
平言莫绕，宜疏莫密。
行文如水，易懂为王。
勿提特例，皆循此规。
实虽胜纯，识错必究。
若需留证，亦要言明。
不明其理，追根问底。
必有一法，可解谜题。
汝非龟叔，求之故难。
立足当下，行必有方。
行难言喻，所思欠妥。
行易言表，所思可嘉。
名正易识，善莫大焉！
'''


if __name__ == "__main__":

   en_result = stats_text_en(en_text)
   cn_result = stats_text_cn(cn_text)
   print(en_result)
   print(cn_result)




