import string
import jieba
from collections import Counter
import re
""" 
jieba.cut 方法接受三个输入参数: 
需要分词的字符串；
cut_all 参数用来控制是否采用全模式；
HMM 参数用来控制是否使用 HMM 模型 
jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，
可以使用 for 循环来获得分词后得到的每一个词语(unicode)，
或者用jieba.lcut 以及 jieba.lcut_for_search 直接返回 list
"""

def stats_text_cn(text,count):
    if not isinstance(text, str):
        raise ValueError('参数必须是 str 类型')
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    text2 = "".join(cn_characters)
    cn_text = jieba.cut(text2, cut_all=False)
    cn_word_counter = Counter()
    for cn_word in cn_text:
        if len(cn_word) >= 2:
            cn_word_counter[cn_word] += 1
        else:
            pass

    return cn_word_counter.most_common(count)


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


if __name__ =='__main__':
    cn_result = stats_text_cn(cn_text, 10)
    print('统计参数中每个中文汉字出现的次数 ==>\n', cn_result)