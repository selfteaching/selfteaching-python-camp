# 统计参数中每个英文单词出现的次数

def stats_text_en(text):
    elments = text.split()
    words = []
    symbols = ', . * !'
    for elment in elments:
        for symbol in symbols:
            elment = elment.replace(symbol, '')
            if len(elment):
                word.append(elment)
        counter = {}
        word_set = set(words)

        for word in word_set:
            counter[word] = words.count(word)
        # 函数返回值用 return 进行返回,若是 return 返回值为 None
        return sorted(counter.items(), key=lambda x: x[1], reverse=True)


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
    cn_character = []
    for character in text:
        # unicode 中 中文 字符的范围
       if '\u4e00' <= character <= '\u9fff':
           cn_character.append(character)
    counter = {}
    cn_character_set = set(cn_character)
    for character in cn_character_set:
        counter[character] = cn_character.count(character)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)


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
f the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

cn_text = '''
The Zen of Python, by Tim Peters

美胜于丑。 
显式优于隐式。 
简单胜于复杂。 
复杂总比复杂好。 
平的比嵌套的好。 
稀疏胜于稠密
可读性计数。 
特殊情况不足以打破规则。 
尽管实用性胜过纯洁性。 
错误永远不会悄悄地过去。 
除非明确沉默。 
面对悠闲，拒绝猜测的诱惑。 
应该有一种——最好只有一种——显而易见的方法来做到这一点。 
不过，如果不是荷兰语的话，这种方式一开始可能并不明显。
现在总比没有好。 
虽然从来没有比现在更好。 
如果实现很难解释，那是个坏主意。 
如果实现很容易解释，这可能是一个好主意。 
名称空间是一个非常好的主意——让我们做更多的事情吧！
 '''


# 搜索 __name__ == __main__
# 一般情况下在文件内 测试 代码的时候以下面的形式进行
if __name__ == '__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n', en_result)
    print('统计参数中每个中文汉字出现的次数 ==>\n', cn_result)