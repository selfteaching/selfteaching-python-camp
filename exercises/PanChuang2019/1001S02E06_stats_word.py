def stats_text_en(text):
    elements= text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element):
            words.append(element)
    counter={}
    word_set=set(words)

    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

def stats_text_cn(text):
    cn_characters=[]
    for character in text:
        if '\u4e00'<= character<='\u9fff':
            cn_characters.append(character)
    counter={}
    cn_character_set=set(cn_characters)
    for character in cn_character_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

en_text='''
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
假如生活没有给你女朋友，
不要悲伤，
不要心急，
忧郁的日子需要的是镇静，
相信吧，
娶媳妇儿的日子将会到来
...
一切都是肾虚，
一切都将过去，
而那春梦中的，
就将变成亲切的怀恋。
'''
if __name__=='__main__':
    en_turnout = stats_text_en(en_text)
    cn_turnout = stats_text_cn(cn_text)
    print('统计参数中每个英文出现的次数\n',en_turnout)
    print('统计参数中每个汉字出现的次数\n',cn_turnout)