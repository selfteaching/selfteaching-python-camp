
#将英文进行词频统计。
def stats_text_en(text):
    #去除字符串中的中文字符
    for chara in text:
        if '\u4e00' <= chara <= '\u9fa5':
            text = text.replace(chara,",")
    #清洗英文字符串中的特殊字符
    for chara in ",.!-*？，。：「」、”":
        text = text.replace(chara," ")
    #将字符串中的英文全部变成小写
    text = text.lower()
    list1 = text.split()
    counts = {}
    #统计每个单词出现的词频
    for word in list1:
        counts[word] = counts.get(word,0) + 1
    list2 = list(counts.items())
    #将单词词频进行降序排序
    list2.sort(key=lambda x:x[1], reverse=True)
    return print(list2)

#将中文进行词频统计。
def stats_text_cn(text):
    list1 = []
    counts = {}
    #选取字符串中的中文字符
    for chara in text:
        if '\u4e00' <= chara <= '\u9fa5':
            list1.append(chara)
    #统计字符串中的中文词频
    for i in list1:
        counts[i] = counts.get(i,0) + 1
    list2 = list(counts.items())
    #将统计后的中文词频按降序排序
    list2.sort(key=lambda x: x[1], reverse=True)
    return print(list2)

text = '''
愚公移山
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
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked yugong’s way making it inconvenient for him and his family to get around.
One day yugong gathered his family together and said,”Let’s do our best to level these two mountains. We shall open a road that leads to Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered his wife. “How on earth do you suppose you can level Mount Taixin and Mount Wanwu? Moreover, where will all the earth and rubble go?”
“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and remove the earth. They transported the earth and rubble to the Sea of Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed Yugong saying,”Aren’t you foolish, my friend? You are very old now, and with whatever remains of your waning strength, you won’t be able to remove even a corner of the mountain.
Yugong uttered a sigh and said,”A biased person like you will never understand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, my grandchildren, my great grandchildren, my great great grandchildren. They descendants will go on forever. But these mountains will not grow any taler. We shall level them one day!” he declared with confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and his crew were, they were struck with fear and reported the incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered two mighty gods to carry the mountains away.
'''

stats_text_en(text)
stats_text_cn(text)

#清洗字符串中的特殊字符,使其仅对文字进行排序。
def data_cleaning(data_sample_str):
    for chara in ",.!-*，。？！ \n":
        data_sample_str = data_sample_str.replace(chara," ")
    return data_sample_str

#将清洗后的英文字符串进行词频统计。
def stats_text_en(text):
    text = text.lower()
    list1 = text.split()
    counts = {}
    for word in list1:
        counts[word] = counts.get(word,0) + 1
    list2 = list(counts.items())
    list2.sort(key=lambda x:x[1], reverse=True)
    print(list2)

#将清洗后的中文字符串进行词频统计。
def stats_text_cn(text):
    counts = {}
    for i in text:
        counts[i] = counts.get(i,0) + 1
    list2 = list(counts.items())
    list2.sort(key=lambda x: x[1], reverse=True)
    print(list2)

#主函数调用上述所有函数。
def main():
    text_en = """
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
    """
    text_cn='''
    蜀道难
    噫吁嚱，危乎高哉！
    蜀道之难，难于上青天！
    蚕丛及鱼凫，开国何茫然！
    尔来四万八千岁，不与秦塞通人烟。
    西当太白有鸟道，可以横绝峨眉巅。
    地崩山摧壮士死，然后天梯石栈相钩连。
    上有六龙回日之高标，下有冲波逆折之回川。
    黄鹤之飞尚不得过，猿猱欲度愁攀援。
    青泥何盘盘，百步九折萦岩峦。
    扪参历井仰胁息，以手抚膺坐长叹。
    问君西游何时还？畏途巉岩不可攀。
    但见悲鸟号古木，雄飞雌从绕林间。
    又闻子规啼夜月，愁空山。
    蜀道之难，难于上青天，使人听此凋朱颜。
    连峰去天不盈尺，枯松倒挂倚绝壁。
    飞湍瀑流争喧豗，砯崖转石万壑雷。
    其险也如此，嗟尔远道之人胡为乎来哉！
    剑阁峥嵘而崔嵬，一夫当关，万夫莫开。
    所守或匪亲，化为狼与豺。
    朝避猛虎，夕避长蛇；磨牙吮血，杀人如麻。
    锦城虽云乐，不如早还家。
    蜀道之难，难于上青天，侧身西望长咨嗟！
    '''
    string1 = data_cleaning(text_en)
    stats_text_en(string1)
    string2 = data_cleaning(text_cn)
    stats_text_cn(string2)

main()

