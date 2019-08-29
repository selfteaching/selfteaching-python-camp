# 1. 定义⼀一个名为 stats_text_en 的函数，函数接受⼀个 字符串 text 作为参数
def stats_text_en(text):

# 2. 实现该函数的功能(同day5任务2):统计参数中每个英⽂文单词出现的次数，最后返回⼀个按词频 降序 排列列的 数组
    if type(text) != str:
        raise ValueError('非字符串类型')
    elements = text.split()   # list。构成函数体的语句从下一行开始，并且必须缩进。
    words = []
    '''
    for x in text:
        for x in ',','.','?','"','!','，','。','？','！','：','「','」':
	        text=text.replace(x,"")
    '''
    symbols = ',*!*.-:？"，。、！「」？：'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        if len(element) and element.isascii():      # 看单词长度是否大于0，大于0则为真正的单词。用str类型的siascii判断是否为英文单词
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
Simple is better than complex.s
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
    if type(text) != str:
        raise ValueError('非字符串类型')

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
愚公移山  How The Foolish Old Man Moved Mountains

太行，王屋二山的北面，住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，擋住去路，使他和家人往來極為不便。

一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，你們認為怎樣？」
大家都異口同聲贊成，只有他的妻子表示懷疑，並說：「你連開鑿一個小丘的力量都沒有，怎可能剷平太行、王屋二山呢？況且，鑿出的土石又丟到哪裏去呢？」

大家都熱烈地說：「把土石丟進渤海裏。」
於是愚公就和兒孫，一起開挖土，把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地走來幫忙。
寒來暑往，他們要一年才能往返渤海一次。

住在黃河河畔的智叟，看見他們這樣辛苦，取笑愚公說：「你不是很愚蠢嗎？你已一把年紀了，就是用盡你的氣力，也不能挖去山的一角呢？」

愚公歎息道：「你有這樣的成見，是不會明白的。你比那寡婦的小兒子還不如呢！就算我死了，還有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有一天，我們會把它們剷平。」

智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大力神揹走二山。
'''

def  stats_text(text):
    return stats_text_en(text) + stats_text_cn(text)   # 两者返回值都是list类型，所以可以用加号

# 搜索 name__==__main__
# 一般情况下在文件中测试代码的时候，以以下形式进行
'''
if __name__=='__main__':
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数==>\n',en_result)
    print('统计参数中每个中文汉字出现的次数==>\n', cn_result)
'''





