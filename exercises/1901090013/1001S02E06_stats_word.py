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
美丽总比丑陋好。
显式比隐式好。
简单总比复杂好。
复杂总比复杂好。
平的比嵌套的好。
稀疏总比密集好。
可读性。
特殊情况还不足以打破规则。
虽然实用性胜过纯洁性。
错误不应该悄无声息地过去。
除非显式地沉默。
面对敏锐，拒绝猜测的诱惑。
应该有一种——最好只有一种——显而易见的方法
它。
不过，除非你是荷兰人，否则这种方式一开始可能并不明显。
现在总比不做好。
虽然从来没有比“现在”更好。
如果实现很难解释，这是一个坏主意。
如果实现很容易解释，这可能是一个好主意。
名称空间是一个很棒的主意——让我们做更多这样的事情!
'''
def stats_text_en(text):
    elements = en_text.split()
# print(elements)
    words = []
    symbols = ',.-!*'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        if len (element):
            words. append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] = words. count(word)

    return sorted(counter.items(), key=lambda x: x[1], reverse=True)



def stats_text_cn(text):
    cn_characters = []
    for character in text:
        if '\u4c00' <= character <= '\u9ffff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)



if __name__ == "__main__":
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数每个英文单词出现的次数 ==>\n', en_result)
    print('统计参数每个中文单词出现的次数 ==>\n', cn_result)