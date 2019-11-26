def stats_text_en(text):
    """统计参数中英文单词出现的次数，并按降序排列数组"""
    if not isinstance(text,str):
        raise ValueError("参数必须是字符串类型，输入类型 %s" % type(text))
    elements=text.split()
    words=[]
    symbols=",.*-!"
    for element in elements:
        for symbol in symbols:
           element=element.replace(symbol,"")
        if len(element) and element.isascii():
           words.append(element)
    print("正常英文单词",words)
    counter={}
    word_set=set(words)
    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

def stats_text_cn(text):
    """统计汉字出现的次数，并按降序排列数组"""
    if not isinstance(text,str):
        raise ValueError("参数必须是字符串类型，输入类型 %s" % type(text))
    cn_courter=[]
    for courter in text:
        if '\u4e00'<= courter <='\u9fff':
            cn_courter.append(courter)
    counter_text={}
    for i in set(cn_courter):
        counter_text[i]=cn_courter.count(i)
    return sorted(counter_text.items(),key=lambda x: x[1],reverse=True)

def stats_text(text):
    """输出合并词频统计结果"""
    if not isinstance(text,str):
        raise ValueError("参数必须是字符串类型，输入类型 %s" % type(text))
    return stats_text_en(text) + stats_text_cn(text)



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
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
cn_text="""
python学习
好好学习
天天向上
"""
if __name__ == "__main__":
    first=stats_text_en(en_text)
    print("统计英文单词出现次数: ",first)
    second=stats_text_cn(cn_text)
    print("统计汉字出现次数: ",second)
