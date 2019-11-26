#定义一个名为 stats_text_en的函数
def stats_text_en(text):
    #创建一个空白的文档以便储存整理过的单词
    words=[]
    #使用split（）去除非英文单词符号
    elements = text.split()
    symbols = ', . * !'
    for element in elements:
        for symbols in symbols:
            element =element.replace(symbols,'')
        if len(element) and element.isascii():
            words.append(element)
    #统计英文单词中出现的次数
    wordfreq = {}
    wordset = set(words)
    for word in wordset:
        wordfreq[word] = words.count(word)
    #返回降序排列的数组
    return sorted(wordfreq.items(),key=lambda k: k[1],reverse=True)

#定义一个名为 stats_text_cn的函数
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        # unicode 中 中文 字符的范围
        if '\u4e00' <= character <='\u9fff':
             cn_characters.append(character)
    #统计中文汉字出现的次数
    characterfreq = {}
    characterset = set(cn_characters)
    for character in characterset:
        characterfreq[character] = cn_characters.count(character)
    #返回降序排列的汉字出现的次数
    return sorted(characterfreq.items(),key=lambda x: x[1],reverse=True)


text = '''
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

print(stats_text_en(text))

text = '''
分析资产需求的简化方法
均衡的理念
对利润的要求
'''

print(stats_text_cn(text))

#合并显示中文及英文字符数量
def stats_text(text):
    '''
    合并显示中文及英文字符数量
    '''
    return stats_text_en(text) + stats_text_cn(text)