
def stats_text_en(text):
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))
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


def stats_text_cn(text):
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)

    return sorted(counter.items(), key=lambda x: x[1], reverse=True)

def stats_text(test):
    ''' 
    合并 英文词频 和 中文字频 的结果
    '''
    return stats_text_en(test) + stats_text_cn(test)


en_test = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit.
Simple is better than complex. Complex is better than complicated. 
Flat is better than nested. Sparse is better than dense. 
Readability counts. Special cases aren't special enough to break the rules. 
Although practicality beats purity. Errors should never pass silently.
Unless explicitly silenced. In the face of ambxiguity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
''' 

cn_text = '''
美丽胜过丑陋。显式优于隐式。
简单比复杂更好。复杂比复杂更好。
扁平优于嵌套。稀疏优于密集。
可读性很重要。特殊情况不足以打破规则。
虽然实用性胜过纯洁。错误不应该默默地传递。
除非明确沉默。面对困惑，拒绝猜测的诱惑。
应该有一个，最好只有一个，明显的方法来做到这一点。
虽然这种方式起初可能并不明显，除非你是荷兰人。
现在比永远好。
虽然现在永远不会比现在好。
如果实施很难解释，这是一个坏主意。
如果实现很容易解释，那可能是个好主意。
命名空间是一个很棒的主意。让我们做更多的事情吧！
''' 


if __name__ == '__main__':
    en_result = stats_text_en(en_test)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n', en_result)
    print('统计参数中每个中文汉字出现的次数 ==>\n', cn_result)
    
