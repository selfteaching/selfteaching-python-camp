from collections import Counter
import jieba

# 统计参数中每个英文单词出现的次数
def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element)and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text,count):
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)


def stats_text(text,count):
    '''
    合并 英文词频 和 中文词频 的结果
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型，输入类型%s'% type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)
    

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
美比丑好，明比涩强。
简胜于繁，繁强于难。
平言莫绕，宜疏莫密。
行文如水，易懂为王。
勿提特例，皆循此规。
实虽胜纯，识错必究。
若需留证，亦要言明。
不明其理，追根问底。
必有一法，可解谜题。
汝非龟叔，求之故难。
立足当下，行必有方。
行难言喻，所思欠妥。
行易言表，所思可嘉。
名正易识，善莫大焉！
'''


if __name__ == "__main__":

   en_result = stats_text_en(en_text)
   cn_result = stats_text_cn(cn_text)
   print(en_result)
   print(cn_result)











    






