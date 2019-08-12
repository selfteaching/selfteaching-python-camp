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

#封装统计英文单词词频的函数
#定义一个名为 stats_text_en 的函数，函数接受一个字符串 text 作为参数
#统计参数中每个英文单词出现的次数，最后返回个按词频降序排列的数组
#为 stats_text_en 添加注释说明
def stats_text_en(text):
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
    return sorted(counter.items(), key=lambda x:x[1],reverse=True)

#封装统计中⽂文汉字字频的函数
#定义一个名为 stats_text_cn 的函数，函数接受⼀个字符串 text 作为参数
#实现该函数的功能:统计参数中每个中文汉字出现的次数，最后返回⼀个按字频降序排列的数组
#为 stats_text_cn 添加注释说明
cn_text='''
python 之禅 by Tim Peters
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即使假借特例的实用性之名，也不可违背这些规则
不要包容所有错误，除非你确定需要这样做
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是 python 之父
做也许好过不做，但不假思索就动手还不如不做
'''

def stats_text_cn(text):
    cn_characters = []
    for character in text:
            #unicode中 中文字符的范围
            if '\u4e00' <= character <='\u9fff':
                cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(), key=lambda x:x[1],reverse=True)

#添加一个名为 stats_text 的函数，实现功能:分别调用stats_text_en , stats_text_cn ，输出合并词频统计结果
#为 stats_text 添加注释说明

#合并英文词频和中文字频的结果
def stats_text(text):
    return stats_text_en(text) + stats_text_cn(text)

#搜索 _name_ == _main_
if __name__ =='__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print(en_result)
    print(cn_result)