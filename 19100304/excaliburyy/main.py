# 19100304 day9 银零
# 1.读取本地文件 tang300.json 进行词频统计
# 2.出书词频最高的前100个词

# 19100304 day8 银零
# 1.调用 stats_word 中的任何一个函数，参数穿入非字符串，验证参数检查功能是否有效
# 2.调用 stats_word 的地方加上 try...except 捕获异常，通过 print 打出方便自己调试的提示信息，让程序正常运行完毕。

# 19100304 day7 银零
# 1.通过模块导入 stats_word, 调用 stats_text 函数统计字符串样本中中文汉字和英文单词出现的次数
# 2.将结果打印出来

# Q:合用时，英文单个字母与中文单句也进行了统计。

import sys                                  #导入模块sys
from stats_word import stats_text           #导入模块 stats_word 中的函数 stats_text

# 直接从pdf文档复制中文文字会出现乱码，解决方法暂时有两个：
# 1.通过ORC软件识别
# 2.从作业库中其他同学提交的作业中复制文本

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

# 1.调用 stats_word 中的任何一个函数，参数穿入非字符串，验证参数检查功能是否有效(day8)

# ：已验证，有效。


# 2.调用 stats_word 的地方加上 try...except 捕获异常，通过 print 打出方便自己调试的提示信息，让程序正常运行完毕。(day8)

try:
    stats_text(text)
except ValueError:
    print(ValueError)


import os
from stats_word import stats_text_cn

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'tang300.json')) as text2:
    text3 = text2.read()
    text4 = stats_word.stats_text_cn(text3,100)
    text2.close()

                 





