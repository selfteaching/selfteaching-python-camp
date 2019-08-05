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
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
#统计参数中每个英⽂单词出现的次数
def stats_text_en(text):              #定义函数
    elements = text.split()           #整理字符
    words = []                        #建立列表
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')             #清除符号
        if len(element):
            words.append(element)                             #将字符加入word列表
    counter = {}                                              #建立字典
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)         #统计每个英文单词出现的次数
        print('英文单词出现的次数 ==>', counter)   
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)   
if __name__ == '__main__':
    print('英文单词词频降序排列 \n', stats_text_en(text))

text1 = '''
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特例的实用性之名，也不可违背这些规则
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是 Python 之父
做也许好过不做，但不假思索就动手还不如不做
如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然
命名空间是一种绝妙的理念，我们应当多加利用
'''
#统计参数中每个中⽂单词出现的次数
def stats_text_cn(text1):          #定义函数
    cn_characters = []
    for character in text1:
        if '\u4e00' <= character <= '\u9fff':    #设置中文字符的范围
            cn_characters.append(character)
    counter={}                                  #建立字典
    cn_character_set=set (cn_characters)
    for character in cn_character_set:
        counter[character]=cn_characters.count(character)          #统计每个中文汉字出现的次数
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)
if __name__ == '__main__':
    print('中文词频降序排列 \n', stats_text_en(text))