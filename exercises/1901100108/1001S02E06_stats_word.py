def stats_text_en(text):
    """这是一个统计字符串中每个英文单词出现次数的函数"""

    #首先，分割文本为单词，但会有标点符号，后面还需要处理掉
    words01 = text.split()
    #定义一个空列表，用于存储处理后的单词们
    words02 = []
    #定义需要删除的标点
    symbols = ',.-*'
    #用空字符替换的方法删除标点符号
    for word01 in words01:
        for symbol in symbols:
            word01 = word01.replace(symbol,'')
        if len(word01) and word01.isascii():
            words02.append(word01)
    #初始化一个字典
    counter = {}
    words_set = set(words02)
    #统计单词出现次数
    for word in words_set:
        counter[word] = words02.count(word) #完成键值的匹配，即生成了字典的元素们
    return sorted(counter.items(), key = lambda x : x[1], reverse=True)

def stats_text_cn(text):
    """这是一个统计字符串中每个汉字出现次数的函数"""
    item_cn = []
    for item in text:
        if '\u4e00' <= item <= '\u9fff':
            item_cn.append(item)
    counter = {}
    item_cn_set = set(item_cn)
    for item1 in item_cn_set:
        counter[item1] = item_cn.count(item1)
    return sorted(counter.items(), key = lambda x: x[1], reverse = True)

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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

cn_text = '''
找活干，是应用所学的最有效方式，有活干，所以就有问题需要解决，所以就有机会反复攻关，在这个过程中，以用带练……
所以，很多人在很多事上都想反了。人们常常取笑那些呼哧呼哧干活的人，笑着说，“能者多劳”，觉得他们有点傻。这话真的没错。但这么说更准：劳者多能 —— 你看，都想反了吧？到最后，一切自学能力差的人，外部的表现都差不多，都起码包括这么一条：眼里没活。他们也不喜欢干活，甚至也没想过，玩乐也是干活（每次逢年过节玩得累死那种） —— 从消耗或者成本的角度来看根本没啥区别 —— 只不过那些通常都是没有产出的活而已。在最初想不出有什么用处的时候，还可以退而求其次，看看 “别人想出什么用处没有？” —— 比如，我去 Google best applications of python skill，在第一个页面我就发现了这么篇文章：“What exactly can you do with Python? ”，翻了一会儿觉得颇有意思……
'''


#以下是刚学到的，用于测试代码用

if __name__ == '__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('参数中,每个英文单词出现的次数\n', en_result)
    print('参数中,每个汉字出现的次数\n', cn_result)

