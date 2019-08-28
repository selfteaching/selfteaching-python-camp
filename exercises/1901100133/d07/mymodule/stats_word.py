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
cn_text='''
python之禅 by Tim peters
优美胜于丑陋
明了胜于晦涩
简洁胜于复杂
复杂胜于凌乱
扁平胜于嵌套
间隔胜于紧凑
可读性很重要
即便假借特例的实用性之名，也不可违背这些规则
不要包容这些错误，除非你确定这样做
当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案
虽然这样不容易，因为你不是python之父
你也许好过不做，但不假思索就做还不如不做
'''


def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    counter={}
    word_set=set(words)
    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(),key=lambda x:x[1], reverse=True)
def stats_text_cn(text):
    cn_characters=[]
    for character in text:
        if '\u4e00'<= character<='\u9fff':
            cn_characters.append(character)
    counter={}
    cn_character_set=set(cn_characters)
    for character in cn_character_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1], reverse=True)

def stats_text(text):
    '''
    合并英文词频和中文词频的结果
    '''
    return stats_text_en(text) + stats_text_cn(text)


if __name__=='__main__':
    en_result=stats_text_en(en_text)
    cn_result=stats_text_cn(cn_text)
    print(en_result)
    print(cn_result)