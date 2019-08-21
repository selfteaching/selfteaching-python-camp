from mymodule import stats_word

sample_text='''
愚公移山

太行，王屋二山的北面住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，擋住去路，使他和家人往來極為不便。
一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，你們認為怎樣？」
大家都異⼝同聲贊成，只有他的妻子表示懷疑，並說：「你連開鑿一個小丘的力量都沒有，怎可能剷平太山、王屋二山呢？況且，鑿出的土石又丟到哪裏去呢？」

大家都熱烈地說：「把土石丟進渤海裏。」
於是愚公就和兒孫，一起開挖土，把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八岁歲也興致勃勃地⾛來幫忙。
寒來暑往，他們要⼀一年才能往返渤海一次。
住在⿈河河畔的智叟，看⾒他們這樣⾟苦，取笑愚公說：「你不是很愚蠢嗎？你已一把年紀了，就是用盡你的氣力，也不能挖去山的一⻆呢？」

愚公歎息道：「你有這樣的成见，是不會明白的。你比那寡婦的小兒子還不如呢！就算我死
了，還有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有一天，我們會把它們剷平。」

智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大力神揹走二山。

How The Foolish Old Man Moved Mountains

Yugong was a ninety-year-old man who lived at the north of two highmountains, Mount Taixing and Mount Wangwu.

Stretching over a wide expanse of land, the mountains blockedyugong’s way making it inconvenient for him and his family to get
around.

One day yugong gathered his family together and said,”Let’s do ourbest to level these two mountains. We shall open a road that leads
to Yuzhou. What do you think?”

All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” mutteredhis wife. “How on earth do you suppose you can level Mount Taixin
and Mount Wanwu? Moreover, where will all the earth and rubble go?”“Dump them into the Sea of Bohai!” said everyone.

So Yugong, his sons, and his grandsons started to break up rocks andremove the earth. They transported the earth and rubble to the Sea
of Bohai.

Now Yugong’s neighbour was a widow who had an only child eight yearsold. Evening the young boy offered his help eagerly.

Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respectedfor his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”

Yugong uttered a sigh and said,”A biased person like you will neverunderstand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, mygrandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will notgrow any taler. We shall level them one day!” he declared with
confidence.

The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugongand his crew were, they were struck with fear and reported the
incident to the Emperor of Heavens.

Filled with admiration for Yugong, the Emperor of Heavens ordered
two mighty gods to carry the mountains away.
'''

result = stats_word.stats_text(sample_text)

print('统计结果 ==>', result)
#下面这句是调用模块中的stats_text函数对么,然后stats_text函数又是调用了stats_text_cn和 stats_text_en
# 两个函数，对吧，然后咱去看stats_text函数，看起来也没有什么错误啊，是吧
# 然后就猜测，是不是stats_text_cn和stats_text_en这两个函数的问题导致的 呢
# result = stats_word.stats_text(sample_text)

# print('统计结果 ==>', result)

# 在这里测试下stats_text_cn函数，为了方便查看，我先把stats_text注释掉行吧
# 下面是测试stats_text_cn,运行一下，看起来是不是没有问题啊

# res1 = stats_word.stats_text_cn(sample_text)
# print(res1)

# 然后就声stats_text_en没有测试了，下面测试下，一样的，我先把上边的注释掉,运行下，发现问题来了
# stats_text_en是统计英文单词的，怎么会有中文，是不是问题就定位到stats_text_en函数中了,然后就到
# stats_texxt_en中找问题
#res2 = stats_word.stats_text_en(sample_text)
#print(res2)
