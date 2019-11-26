# 统计参数中每个英文单词出现的次数
# 此为视频答案
def stats_text_en(text):
	if not isinstance(text, str):
		raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))
	elements = text.split()
	words = []
	symbols = ',.*-!?'
	for element in elements:
		for symbol in symbols:
			element = element.replace(symbol, '')
		if len(element) and element.isascii():
			words.append(element)
	
	counter = {}
	word_set = set(words)

	for word in word_set:
		counter[word] = words.count(word)

	return sorted(counter.items(), key=lambda x:x[1], reverse=True)
	# print(sorted(counter.items(), key=lambda x:x[1], reverse=True))


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text):
	if not isinstance(text, str):
		raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))
	cn_characters = []
	for character in text:
		# unicode中 中文字符的范围
		if '\u4e00' <= character <= '\u9fff':
			cn_characters.append(character)
	
	counter = {}
	cn_character_set = set(cn_characters)
	
	for character in cn_character_set:
		counter[character] = cn_characters.count(character)
	return sorted(counter.items(), key=lambda x:x[1], reverse=True)



def stats_text(text):
	if not isinstance(text, str):
		raise ValueError('参数必须是 str 类型，输入类型 %s' % type(text))	
	return stats_text_en(text) + stats_text_cn(text)




en_text = '''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

cn_text = '''
如果你不觉得正则表达式很难读写的话，要么你是一个天才，要么，你不是地球人。正则表达式的语法很令人头疼，即使对经常使用它的人来说也是如此。由于难于读写，容易出错，所以找一种工具对正则表达式进行测试是很有必要的。
'''

# 测试代码
# if __name__ == '__main__':
# 	en_result = stats_text_en(en_text)
# 	cn_result = stats_text_cn(cn_text)
# 	print('英文单词出现的次数 ==>\n', en_result)
# 	print('中文汉字出现的次数 ==>\n', cn_result)

text = '''
愚公移⼭山

太⾏行行，王屋⼆二⼭山的北北⾯面，住了了⼀一個九⼗十歲的⽼老老翁，名叫愚公。⼆二⼭山佔地廣闊，擋住去路路，使他
和家⼈人往來來極為不不便便。

⼀一天，愚公召集家⼈人說：「讓我們各盡其⼒力力，剷平⼆二⼭山，開條道路路，直通豫州，你們認為怎
樣？」
⼤大家都異異⼝口同聲贊成，只有他的妻⼦子表示懷疑，並說：「你連開鑿⼀一個⼩小丘的⼒力力量量都沒有，怎
可能剷平太⾏行行、王屋⼆二⼭山呢？況且，鑿出的⼟土⽯石⼜又丟到哪裏去呢？」

⼤大家都熱烈烈地說：「把⼟土⽯石丟進渤海海裏。」
於是愚公就和兒孫，⼀一起開挖⼟土，把⼟土⽯石搬運到渤海海去。
愚公的鄰居是個寡婦，有個兒⼦子⼋八歲也興致勃勃地⾛走來來幫忙。
寒來來暑往，他們要⼀一年年才能往返渤海海⼀一次。

住在⿈黃河河畔的智叟，看⾒見見他們這樣⾟辛苦，取笑愚公說：「你不不是很愚蠢嗎？你已⼀一把年年紀
了了，就是⽤用盡你的氣⼒力力，也不不能挖去⼭山的⼀一⻆角呢？」

愚公歎息道：「你有這樣的成⾒見見，是不不會明⽩白的。你⽐比那寡婦的⼩小兒⼦子還不不如呢！就算我死
了了，還有我的兒⼦子，我的孫⼦子，我的曾孫⼦子，他們⼀一直傳下去。⽽而這⼆二⼭山是不不會加⼤大的，總有
⼀一天，我們會把它們剷平。」

智叟聽了了，無話可說：
⼆二⼭山的守護神被愚公的堅毅精神嚇倒，便便把此事奏知天帝。天帝佩服愚公的精神，就命兩位⼤大
⼒力力神揹⾛走⼆二⼭山。

How The Foolish Old Man Moved Mountains

Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.

Stretching over a wide expanse of land, the mountains blocked
yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do our
best to level these two mountains. We shall open a road that leads
to Yuzhou. What do you think?”

All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered
his wife. “How on earth do you suppose you can level Mount Taixin
and Mount Wanwu? Moreover, where will all the earth and rubble go?”
“Dump them into the Sea of Bohai!” said everyone.

So Yugong, his sons, and his grandsons started to break up rocks and
remove the earth. They transported the earth and rubble to the Sea
of Bohai.

Now Yugong’s neighbour was a widow who had an only child eight years
old. Evening the young boy offered his help eagerly.

Summer went by and winter came. It took Yugong and his crew a full
year to travel back and forth once.

On the bank of the Yellow River dwelled an old man much respected
for his wisdom. When he saw their back-breaking labour, he ridiculed

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
When the guardian gods of the mountains saw how determined Yugong
and his crew were, they were struck with fear and reported the
incident to the Emperor of Heavens.

Filled with admiration for Yugong, the Emperor of Heavens ordered
two mighty gods to carry the mountains away.
'''

if __name__ == '__main__':
	stats_text_en(en_text)
# if __name__ == '__main__':
# 	stats_text(cn_text)