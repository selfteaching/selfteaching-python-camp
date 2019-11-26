
#统计参数中每个英文单词出现次数
def stats_text_en(text): 
    elements = text.split()
    words = []
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)
    counter = {}
    word_set = set(words)

    for word in word_set:
        counter[word] = word.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

#统计参数中每个中文字出现的次数
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter={}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


def stats_text(text):
    '''
    合并英文词频和中文词频的结果
    '''

    return stats_text_en(text)+stats_text_cn(text)







text_en = '''
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

text_cn = '''
当我和世界不一样
那就让我不一样
坚持对我来说就是以刚克刚
我如果对自己妥协
如果对自己说谎
即使别人原谅
我也不能原谅
最美的愿望一定最疯狂
我就是我自己的神
在我活的地方
我和我最后的倔强
握紧双手绝对不放
下一站是不是天堂
就算失望不能绝望
我和我骄傲的倔强
我在风中大声地唱
这一次为自己疯狂
就这一次 我和我的倔强
'''
if __name__ == '__main__': 
    en_results=stats_text_en(text_en) 
    print('参数中每个英文单词出现的次数 \n', en_results) 
    cn_results=stats_text_cn(text_cn) 
    print('参数中每个中文字出现的次数 \n', cn_results)