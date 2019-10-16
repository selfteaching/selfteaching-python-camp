def stats_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element):
            words.append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word] = words.count(word)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)


def stats_text_cn(text):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

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

cn_text = '''       
小时候
乡愁是一枚小小的邮票
我在这头
母亲在那头
长大后
乡愁是一张窄窄的船票
我在这头
新娘在那头
后来啊
乡愁是一方矮矮的坟墓
我在外头
母亲在里头
而现在
乡愁是一湾浅浅的海峡
我在这头
大陆在那头
'''
if __name__ == '__main__':
    en_text = 'english'
    cn_text = '中文'
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数 ==>\n',en_result)
    print('统计参数中每个中文单词出现的次数 ==>\n',cn_result)