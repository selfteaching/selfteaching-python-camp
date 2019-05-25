
from mymodule import stats_word_d08
try:
    stats_word_d08.stats_text_en(12123)
except ValueError as e:
    print(e)
sample_text = '''

愚公移山
太行，王屋二山的北面住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，擋住去路，使他
和家人往來極為不便。
一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，你們認為怎
樣？」
大家都異口同聲贊成，只有他的妻子表示懷疑，並說：「你連開鑿一個山丘的力量都沒有，怎
可能剷平太行、王屋二山呢？況且，鑿出的土石又丟到哪裏去呢？」
大家都熱烈地說：「把土石丟進渤海裏。」
於是愚公就和兒孫，一起開挖二山把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地过來幫忙。
寒來暑往，他們要一年才能往返渤海一次。
住在黄河河畔的智叟，看见他們這樣辛苦，取笑愚公說：「你不是很愚蠢嗎？你已经把年紀
了，就是用盡你的氣力，也不能挖去山的一⻆呢？」
愚公歎息道：「你有這樣的成见，是不會明白的。你比那寡婦的小兒还還不如呢！就算我死
了，還有我的兒子、我的孫子、我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有
一天，我們會把它們剷平。」
智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大力神揹走二山。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two highmountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do ourbest to level these two mountains. We shall open a road that leads
to Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered his wife. “How on earth do you suppose you can level Mount Taixin
and Mount Wanwu? Moreover, where will all the earth and rubble go?”“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and remove the earth. They transported the earth and rubble to the Sea
of Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will neverunderstand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, mygrandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will notgrow any taler. We shall level them one day!” he declared with
confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugongand his crew were, they were struck with fear and reported the
incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens orderedtwo mighty gods to carry the mountains away.
'''

result = stats_word_d08.stats_text(sample_text)

print('统计结果==>',result)



'''
可以不带任何异常类型使用except，如下实例：

try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
以上方式try-except语句捕获所有发生的异常。但这不是一个很好的方式，我们不能通过该程序识别出具体的异常信息。因为它捕获所有的异常。

使用except而带多种异常类型
你也可以使用相同的except语句来处理多个异常信息，如下所示：

try:
    正常的操作
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   发生以上多个异常中的一个，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
    '''
======
result = stats_word.stats_text(sample_text)

print('统计结果==>',result)

