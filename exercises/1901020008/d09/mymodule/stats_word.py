from collections import Counter

def stats_text_en(en_text, count):
    elements = en_text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)
   

def stats_text_cn(cn_text, count):
    cn_characters = []
    for character in cn_text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)

def stats_text(en_text, cn_text, count):
    if not isinstance(en_text, cn_text, str):
        raise ValueError('非字符串类型')
    return stats_text_en(en_text, count) + stats_text_cn(cn_text,count)

if __name__ == '__main__':
    en_text = '''
The Zen of python,by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Comples is better than complicated.
Flat is better than dense.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity,refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain,it may be a good idea.
If the implementation is easy to explain,it may be a good idea.
Namespaces are one honking great idea--let's do more of those!
'''
cn_text = '''
轻轻的我走了

正如我轻轻的来

我轻轻的招手

作别西天的云彩

那河畔的金柳

是夕阳中的新娘

波光里的艳影

在我的心头荡漾

软泥上的青荇

油油的在水底招摇

在康河的柔波里

我甘心做一条水草

那榆荫下的一潭

不是清泉 是天上虹

揉碎在浮藻间

沉淀着彩虹似的梦

寻梦 撑一支长蒿

向青草更青处漫溯

满载一船星辉

在星辉斑斓里放歌

但我不能放歌

悄悄是别离的笙箫

夏虫也为我沉默

沉默是今晚的康桥

悄悄的我走了

正如我悄悄的来

我挥一挥衣袖

不带走一片云彩
'''