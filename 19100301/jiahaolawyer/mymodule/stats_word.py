# 示例字符串
string1 =  '''

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
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。
'''

import collections
import re

def stats_text_en(string_en):
    ''' 统计英文词频

    第一步：过滤英文字符，并将string拆分为list。
    第二步：清理*-等标点符号。
    第三步：使用collections库中的Counter函数进行词频统计并输出统计结果。
    '''
    print("处理前的原始字符串\n\n",string_en)
    result = re.sub("[^A-Za-z]", " ", string_en.strip())#把非A-Z和a-z的字符串全部去除掉
    print("处理后的结果\n\n",result)
    newList = result.split( )
    i=0
    for i in range(0,len(newList)):
        newList[i]=newList[i].strip('*-,.?!')
        if newList[i]==' ': 
            newList[i].remove(' ')
        else:
            i=i+1
    print('英文单词词频统计结果： ',collections.Counter(newList),'\n')


def stats_text_cn(string_cn):
    ''' 统计中文汉字字频

    第一步：过滤汉字字符，并定义频率统计函数 stats()。
    第二步：清除文本中的标点字符,将非标点字符组成新列表 new_list。
    第三步：遍历列表，将字符同上一次循环中频率统计结果作为形参传给统计函数stats()。
    第四步：统计函数在上一次统计结果基础上得出本次统计结果，赋值给newDict。
    第五步：new_list遍历结束，输出倒序排列的统计结果。
    '''
    result1 = re.findall(u'[\u4e00-\u9fff]+', string_cn)
    newString = ''.join(result1)

    def stats(orgString, newDict) :
        d = newDict
        for m in orgString :
            d[m] = d.get(m, 0) + 1
        return d

    new_list = []
    for char in newString :
        cn = char.strip('-*、。，：？！……')
        new_list.append(cn)

    words = dict()
    for n in range(0,len(new_list)) :
        words = stats(new_list[n],words)
    newWords = sorted(words.items(), key=lambda item: item[1], reverse=True) 
    print('中文汉字字频统计结果： ',dict(newWords))

# 调用函数
stats_text_en(string1)
stats_text_cn(string1)
