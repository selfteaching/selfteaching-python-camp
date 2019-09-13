# 统计参数中英文单词出现的次数，并按降序排列
def stats_text_en(text):  #定义函数
    elements = text.split()#对字符串进行切片
    words = []#设置列表
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element):
            words.append(element)
    counter = {}#创建字典
    word_set = set(words)#创建无序不重复集合

    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)

# 统计参数中汉字出现次数，并按降序排列
def stats_text_cn(text):#设定函数
    cn_charactors = []
    for charactor in text:
        if '\u4e00'<= charactor <= '\u9fff':#中文字符的代码区间
            cn_charactors.append(charactor)
    counter = {}#创建字典
    cn_charactor_set = set(cn_charactors)
    for charactor in cn_charactor_set:
        counter[charactor] = cn_charactors.count(charactor)
    return sorted(counter.items(),key=lambda x:x[1], reverse=True)


en_text = '''
the Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!
'''

cn_text = '''
Python之禅 by Tim Peters
 
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
尽管实用会打破纯粹，也不可违背规则 
不要包容任何错误，除非你确定需要这样做 
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是 Python 之父 
做也许好过不做，但不假思索就动手还不如不做 
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然 
命名空间是一种绝妙的理念，请多加利用
'''

if __name__ == "__main__":
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中英文单词出现次数==>\n', en_result)
    print('统计参数中汉字出现次数==>\n', cn_result)