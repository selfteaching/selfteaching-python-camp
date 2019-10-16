# 封装统计英⽂单词词频的函数
def stats_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*-!'

    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():
            words.append(element)

    counter = {}
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)

# 按照出现次数从⼤到⼩输出所有的单词及出现的次数
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)


# 统计参数中每个中⽂汉字出现的次数
def stats_text_cn(text):
    cn_characters = []
    for characters in text:
        if '\u4e00' <= characters <= '\u9fff':
            cn_characters.append(characters)
    counter = {}
    cn_characters_set = set(cn_characters)
    for character in cn_characters_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(), key=lambda x:x[1], reverse=True)


def stats_text(text):  # 合并英文词频和中文字频的结果
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
将进酒

作者：李白

君不见，黄河之水天上来，奔流到海不复回。
君不见，高堂明镜悲白发，朝如青丝暮成雪。
人生得意须尽欢，莫使金樽空对月。
天生我材必有用，千金散尽还复来。
烹羊宰牛且为乐，会须一饮三百杯。
岑夫子，丹丘生，将进酒，杯莫停。
与君歌一曲，请君为我倾耳听。
钟鼓馔玉不足贵，但愿长醉不复醒。
古来圣贤皆寂寞，惟有饮者留其名。
陈王昔时宴平乐，斗酒十千恣欢谑。
主人何为言少钱，径须沽取对君酌。
五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。
'''

if __name__ == "__main__":
    en = stats_text_en(en_text)
    cn = stats_text_cn(cn_text)
    print('英文单词出现的次数：',en)
    print('中文汉字出现的次数：',cn)