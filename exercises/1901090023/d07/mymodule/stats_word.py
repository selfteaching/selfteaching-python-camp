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

On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed Yugong saying,”Aren’t you foolish, my friend? You are very old now, and with whatever remains of your waning strength, you won’t be able to remove even a corner of the mountain.”

Yugong uttered a sigh and said,”A biased person like you will never understand. You can’t even compare with the widow’s little boy!”

“Even if I were dead, there will still be my children, my grandchildren, my great grandchildren, my great great grandchildren. They descendants will go on forever. But these mountains will not grow any taler. We shall level them one day!” he declared with confidence.

The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and his crew were, they were struck with fear and reported the incident to the Emperor of Heavens.

Filled with admiration for Yugong, the Emperor of Heavens ordered two mighty gods to carry the mountains away.
'''


# 将统计中文词频和英文词频的函数封装为一个模块

# 1. 封装统计英文单词次数的函数
def stats_text_en(text):                   # 定义函数，形式参数名为text
    """ 函数名：stats_text_en               # 文档字符串用来为函数添加注释说明

    参数名：text
    统计参数中英文单词词频
    最后返回一个按词频降序排列的数组
    """
    
    text1 = text.replace(';', '').replace('.', '')     # 去掉字符串中的特殊符号
    list1 = text1.split()                              # 字符串转换为列表
   
    d={}                                               # 创建一个空字典d
    for i in list1:                                    # for循环遍历列表, i 为列表中的各个元素
        d[i]=list1.count(i)                            # list1.count(i)是i 单词元素在列表中的次数，将其赋值给字典d中key为i单词元素的value值
    d1=sorted(d.items(),key=lambda x:x[1],reverse=True) # items() 函数以列表返回可遍历的(键, 值) 元组数组；sorted()函数，通过key参数，指定第二个字段（value值）的值的降序来排序
    return d1                                           # python 函数返回值 return，函数中一定要有return返回值才是完整的函数。              【非常重要】
print('统计参数中英文单词出现的次数 ==>\n', stats_text_en(text))
print('_'*200)


# 2. 封装统计中文汉字字频的函数
def stats_text_cn(text):         # 定义函数，用来统计中文汉字字频，并且给函数名添加注释说明
    """ 函数名：stats_text_cn                 # 文档字符串用来为函数添加注释说明

    参数名：text
    统计参数中中文汉字词频
    最后返回一个按词频降序排列的数组
    """

    text = text.replace('。','').replace('、','').replace('', ' ')    # 前两个去掉特殊符号，最后一个是把字符串拆成一个个汉字 【非常重要】
    list1 = text.split()                    # 将字符串转换为列表

    characters = []
    for character in list1:
        if len(character):                       # 如果charater的长度不为0，则算作正常汉字
            characters.append(character)          # characters列表中添加中文汉字元素
    charanum = {}
    character_set = set(characters)              # 去掉列表中重复汉字元素后的集合

    for hanzi in character_set:
        charanum[hanzi] = characters.count(hanzi)
    return sorted(charanum.items(), key=lambda x: x[1], reverse=True)
print('统计参数中中文汉字出现的次数 ==>\n', stats_text_cn(text))
       

# 3. 添加名为stats_text的函数，实现分别调用stats_text_en, stats_text_cn的功能
def stats_text():
    """ 函数名：stats_text

    实现分别调用stats_text_en, stats_text_cn的功能
    """
    stats_text_en
    stats_text_cn