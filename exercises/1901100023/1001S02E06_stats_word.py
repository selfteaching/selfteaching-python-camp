# 1. 定义⼀一个名为 stats_text_en 的函数，函数接受⼀个 字符串 text 作为参数
def stats_text_en(text):

# 2. 实现该函数的功能(同day5任务2):统计参数中每个英⽂文单词出现的次数，最后返回⼀个按词频 降序 排列列的 数组
    elements = text.split()   # list。构成函数体的语句从下一行开始，并且必须缩进。
    words = []
    symbols = ',*!*.-'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element):      # 看单词长度是否大于0，大于0则为真正的单词
            words.append(element)
    counter = {}
    word_set = set(words)
    for word in word_set:
        counter[word]=words.count(word)
    # 函数返回用 return 进行返回，如果没有 return 返回值则为 None
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)
    

en_text= '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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


# ------------------------------------------------------------------------------------------------------------------
# 3. 定义⼀一个名为 stats_text_cn 的函数，函数接受一个字符串串 text 作为参数
# 4. 实现该函数的功能:统计参数中每个中⽂文汉字出现的次数，最后返回⼀个按字频 降序 排列的 数组  
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff':  # unicode中文字符的范围
        # 计算机中所有的字符都是有数字来表示的。汉字也是有数字表示的，
        # Unicdoe4E00~9FFF表示中文
        # if u'a' <= ch <= u'z' or u'A' <= ch <= u'Z':提取英文
            cn_characters.append(character)
        counter = {}
        cn_character_set = set(cn_characters)
        for character in cn_character_set:
            counter[character] = cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)


cn_text = '''
上善若水。
水善利万物而不争，处众人之所恶，故几于道。
居，善地；心，善渊；与，善仁；言，善信；政，善治；事，善能；动，善时。
夫唯不争，故无尤。
'''


# 搜索 name__==__main__
# 一般情况下在文件中测试代码的时候，以以下形式进行
if __name__=='__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数==>\n',en_result)
    print('统计参数中每个中文汉字出现的次数==>\n', cn_result)