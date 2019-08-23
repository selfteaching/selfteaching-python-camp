
import collections

""" 
str.count(sub, start= 0,end=len(string))
用于统计字符串里某个字符出现的次数
sub -- 搜索的子字符串
"""

def stats_text_en(text, count):
    if not isinstance(text, str): # 【检查】参数必须是str类型
        raise ValueError('参数必须是 str 类型')
    elements = text.split()
    words =[]
    symbols =',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '') #删除掉标点符号
        if len(element) and element.isascii():  # element非空切为ascii码
            words.append(element)
    counter = {}
    word_set = set(words) 

    for word in word_set:
        counter[word] = words.count(word) # 向counter字典中添加东西
    """ 
    dict.items() 以列表返回可遍历的(键, 值) 元组数组
    sorted(iterable, cmp=None, key=None, reverse=False)
    key=lambda x: x[1] 的意思是按照元祖数组的第2个元素排序
    """   
    list_en = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return collections.Counter(list_en).most_common(count) 


def stats_text_cn(text,count):
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型')
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff': # 判断元素为中文
            cn_characters.append(character)
    counter = {}
    cn_characters_set = set(cn_characters)
    for character in cn_characters_set:
        counter[character] = cn_characters.count(character)
    list_cn = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return collections.Counter(list_cn).most_common(count) 

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

cn_text ='''
python之禅 
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特例的实用性之名，也不可能违背这些规则
不要包容所有错误，除非你确定需要这样做
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这并不容易，因为你不是python之父
做也许好过不做，但不假思索就动手还不如不做
。。。
'''



def stats_text(text, count): #合并 英文词频  和 中文词频 的结果
    # if (not isinstance(en_text,str)) or (not isinstance(cn_text,str)):
    #     raise TypeError("string is ony the type can be accepted")
    return stats_text_en(text, count) + stats_text_cn(text, count)

""" 
if __name__ == '__main__':
当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
"""
if __name__ =='__main__':
    en_result = stats_text_en(en_text, 100)
    cn_result = stats_text_cn(cn_text, 100)
    print('统计参数中每个英文单词出现的次数 ==>\n', en_result)
    print('统计参数中每个中文汉字出现的次数 ==>\n', cn_result)