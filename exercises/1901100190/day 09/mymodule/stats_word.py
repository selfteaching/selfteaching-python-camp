from collections import Counter

# 统计参数中每个英文单词出现的次数

def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ",.*-!"
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, ' ')
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)
    

# 统计参数中每个中文出现的次数

def stats_text_cn(text, count):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)


def stats_text(text, count):
    '''
    合并 英文单词词频 和 中文汉字字频 的结果
    '''
    if not isinstance(text, str):
        raise ValueError("参数必须是 str类型，输入类型 %s", type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)

if __name__ == "__main__":
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

Although that way may not be obvious at first unless you're Dutch. Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!

'''

cn_text = '''

优美优于丑陋，

明了优于隐晦；

简单优于复杂，

复杂优于凌乱，

扁平优于嵌套，

可读性很重要！

即使实用比纯粹更优，

特例亦不可违背原则。

错误绝不能悄悄忽略，

除非它明确需要如此。

面对不确定性，

拒绝妄加猜测。

任何问题应有一种，

且最好只有一种，

显而易见的解决方法。

尽管这方法一开始并非如此直观，

除非你是荷兰人。

做优于不做，

然而不假思索还不如不做。

很难解释的，必然是坏方法。

很好解释的，可能是好方法。

命名空间是个绝妙的主意，

我们应好好利用它。

'''