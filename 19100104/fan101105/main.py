
from mymodule import stats_word
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
愚公歎息道：「你有這樣的成見，是不會明白的。你比那寡婦的小兒子還不如呢！就算我死了，還有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。
而這二山是不會加大的，總有一天，我們會把它們剷平。」
智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命
兩位大力神揹走二山。
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
'''

testerr1={}

try:
    stats_word.stats_text(testerr1)
except ValueError as r:
    print(r)