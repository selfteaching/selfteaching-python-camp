# count English words and sorted descending 
def stats_text_en(text):
    if not isinstance(text,str):
        raise ValueError("Arguments must be string type, input type %s" % type(text)) 
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        # use "isascii" in str type to check if an element is integer  
        if len(element) and element.isascii():
            words.append(element)
    counter={}
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(), key= lambda x:x[1], reverse=True)

# ount Chinese character and sorted descending
def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError("Arguments must be string type, input type %s" % type(text)) 
    cn_characters=[]
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)        
    counter={}
    cn_characters_set=set(cn_characters)

    for character in cn_characters_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(), key= lambda x:x[1], reverse=True)


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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


cn_text = '''
Python 之禅，by Tim Peters

优美胜于丑陋
明确胜于隐晦
简单胜于复杂
复杂胜于凌乱
扁平胜于嵌套
稀疏胜于紧凑
可读性至关重要
即便特例，也需服从以上规则
除非刻意追求，错误不应跳过
面对歧义条件，拒绝尝试猜测
解决问题的最优方法应该有且只有一个
尽管这一方法并非显而易见（除非你是Python之父）
动手胜于空想
空想胜于不想
难以解释的实现方案，不是好方案
易于解释的实现方案，才是好方案
命名空间是个绝妙的理念，多多益善！'''


def stats_text(text):
    '''
    Consolidate results of stats_text_en and stats_text_cn 
    '''
    if not isinstance(text,str):
        raise ValueError("Arguments must be string type, input type %s" % type(text)) 
    return stats_text_en(text) + stats_text_cn(text)


#testing code 
if  __name__ == "__main__":
    en_results = stats_text_en(en_text)
    cn_results = stats_text_cn(cn_text)
    print('count English words and sorted descending:',en_results)
    print('\ncount Chinese character and sorted descending:',cn_results)





