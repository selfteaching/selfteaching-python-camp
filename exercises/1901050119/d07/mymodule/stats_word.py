text =  '''
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
On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed Yugong saying,”Aren’t you foolish, my friend? You are very old now, and with whatever remains of your waning strength, you won’t be able to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will never understand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, my grandchildren, my great grandchildren, my great great grandchildren. They descendants will go on forever. But these mountains will not grow any taler. We shall level them one day!” he declared with confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and his crew were, they were struck with fear and reported the incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered two mighty gods to carry the mountains away.
'''


# 统计字符串中每个英文单词出现的次数，返回一个按词频降序排列的数组
def stats_text_en (text):

    # 剔除字符串中的无意义字符
    s1 = text.replace('*', '', text.count('*'))
    s2 = s1.replace('-', '', text.count('-'))
    s3 = s2.replace(',', '', text.count(','))
    s4 = s3.replace('.', '', text.count('.'))
    s5 = s4.replace('“', '', text.count('“'))
    s6 = s5.replace('”', '', text.count('”'))
    s7 = s6.replace('’', '', text.count('’'))
    s8 = s7.replace('?', '', text.count('?'))
    text1 = s8.replace('!', '', text.count('!'))

    #拆分字符串为单词列表
    L = text1.split()

    #将单词列表转换以单词为key，以单词个数为value的字典
    i = 0
    aDict = {}

    while i < len(L) :
        cnt = text1.count(L[i])
        aDict.setdefault(L[i], cnt) 
        i = i + 1

    # 将字典中的单词按个数从大到小排序
    L1 = sorted(aDict.items(), key=lambda x: x[1], reverse=True)
    return L1


# 统计字符串中每个中文汉字出现的次数，返回一个按字频降序排列的数组 
def stats_text_cn(text):
    
    # 剔除字符串中的非中文字符
    s1 = text.replace('，', '', text.count('，'))
    s2 = s1.replace('“', '', text.count('“'))
    s3 = s2.replace('”', '', text.count('”'))
    s4 = s3.replace('——', '', text.count('——'))
    s5 = s4.replace('。', '', text.count('。'))
    s6 = s5.replace('……', '', text.count('……'))
    s7 = s6.replace(' ', '', text.count(' '))
    s8 = s7.replace('\n', '', text.count('\n'))
    s9 = s8.replace('「', '', text.count('「'))
    s10 = s9.replace('」', '', text.count('」'))
    s11 = s10.replace('：', '', text.count('：'))
    text1 = s11.replace('？', '', text.count('？'))

    # 将字符串整理为以每个汉字为key，以该汉字个数为value的字典
    i = 0
    bDict = {}
    
    while i < len(text1):
        if ord(text[i]) in range(65, 91):
            break
        elif ord(text[i]) in range(97, 123):
            break
        else:
            cnt = text1.count(text1[i])
            bDict.setdefault(text1[i], cnt) 
            i = i + 1
    
    # 将字典中的中文汉字按个数从大到小排序
    L2 = sorted(bDict.items(), key=lambda x: x[1], reverse=True)
    return L2



# 分别统计字符串中每个中文汉字和英文单词出现的次数，返回一个按频次降序排列的数组 
def stats_text(text):
    # 将字符串中文部分的句号剔除，只留最后一个，作为中英文部分的分隔符，以便将整个字符串拆分为中文和英文两个部分。
    s1 = text.replace('。', '', text.count('。') -1)
    t = s1.partition('。')
    
    # 分别对拆分出来的中、英文部分进行词频统计，并将结果打印出来。
    print(stats_text_cn(t[0]) + stats_text_en(t[2]))