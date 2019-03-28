# -*- encoding:utf-8 -*-
import re

text = '''
􏴉􏴊􏴨􏲔􏰟􏴩􏴪􏳜􏲰􏰯愚公移山
太行，王屋二山的北面，住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，擋住去路，使他和家人往來極為不便。
一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，你們認為怎樣？」
於是愚公就和兒孫，一起開挖土，把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地走來幫忙。
寒來暑往，他們要一年才能往返渤海一次。
住在黃河河畔的智叟，看見他們這樣辛苦，取笑愚公說：「你不是很愚蠢嗎？你已一把年紀了，就是用盡你的氣力，也不能挖去山的一角呢？」
愚公歎息道：「你有這樣的成見，是不會明白的。你比那寡婦的小兒子還不如呢！就算我死了，還有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有一天，我們會把它們剷平。」
智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大力神揹走二山。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked
yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do our
best to level these two mountains. We shall open a road that leads to
Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered his
wife. “How on earth do you suppose you can level Mount Taixin and
Mount Wanwu? Moreover, where will all the earth and rubble go?”
“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and
remove the earth. They transported the earth and rubble to the Sea of
Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years
old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full
year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for
his wisdom. When he saw their back-breaking labour, he ridiculed
Yugong saying,”Aren’t you foolish, my friend? You are very old now,
and with whatever remains of your waning strength, you won’t be able
to remove even a corner of the mountain.”
Yugong uttered a sigh and said,”A biased person like you will never
understand. You can’t even compare with the widow’s little boy!”
“Even if I were dead, there will still be my children, my
grandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will not
grow any taler. We shall level them one day!” he declared with
confidence.
The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and
his crew were, they were struck with fear and reported the incident
to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered two
mighty gods to carry the mountains away.

'''

import re
cn = re.compile(r'[^\u0061-\u007a,\u0020]')
en = re.compile(r'[\u0061-\u007a,\u0020]')
cn = "".join(cn.findall(text.lower()))
en = "".join(en.findall(text.lower()))



frequency = {}
frequency_cn = {}


def stats_text_en(text):
	# substitute useless characters
	replace_text = en.replace('--','').replace(',','').replace('.','').replace('*','').replace('!','').replace('”','').replace('“','').replace('「','').replace('」','').replace('?','').replace('\n','')
	# split the words
	split_text = replace_text.split()
	# creat a new blank dict
	for word in split_text:
	    if word not in frequency:
	    	# if word is not in split_text, creat a new key and let counts be 1
	        frequency[word] = 1
	    else:
	    	# if words is in split_text, let counts added 1
	        frequency[word] += 1

	return frequency
	# return sorted(frequency.items(), key=lambda d: d[1], reverse=True)


def stats_text_cn(text):
	# remove Chinese characters
	replace_text = cn.replace('--','').replace('，','').replace('。','').replace('*','').replace('！','').replace('”','').replace('“','').replace('「','').replace('」','').replace('？','').replace('\n','')
	# set new dict
	# frequency_cn = {}
	# frequency stat
	for word_cn in replace_text:
		if word_cn not in frequency_cn:
			frequency_cn[word_cn] = 1
		else:
			frequency_cn[word_cn] += 1
	return frequency_cn
	# return sorted(frequency_cn.items(), key=lambda d: d[1], reverse=True)


stats_text_en(text)
stats_text_cn(text)
frequency_sum = {**frequency, **frequency_cn}
print(sorted(frequency_sum.items(), key=lambda d: d[1], reverse=True))

# print(sorted(frequency.items(), key=lambda d: d[1], reverse=True))




# print(stats_text_en(text))








