# 第八天作业2
# 2019年3月28日
# 通过导入模块stats_word,调用stats_text,
# 统计英文单词和中文出现次数
# 打印结果

# 调用stats_word模块

# 在调用stats_word的地方采用try……except 捕抓异常


text ='''
	愚公移山 
	太行，王屋二山的北面，住了一涸九十崴的老翁，名叫愚公。二山估地癀阔，挡住去路，使他 
	和家人往来极为不便。 
	一天，愚公召集家人说:「让我们各尽其力，铲平二山，开条道路，直通豫州，你们认为怎 
	样?」 
	大家都巽口同声赞成，只有他的妻子表示怀疑，并说:「你连开挖一小丘的力量都没有，怎 
	可能铲平太行、王屋二山呢?况且，挖出的土石又丢到哪里去呢?」

	大家都熟烈地说:「把土石丢进渤海里。」 
	於是愚公就和儿孙，一起用开挖土，把土石搬运到渤海去。 
	愚公的邻居是个寡妇，有个儿子八岁也兴致勃勃地走来帮忙。 
	寒来暑往，他们要一年才能往返渤海一次。

	住在黄河河畔的智叟，看见他们这样辛苦，取笑愚公说:「你不是很愚蠢吗?你已一把年纪
	了，就是用蛊你的氯力，也不能挖去山的一角呢?J 
	愚公叹息道:「你有这样的成见，是不曾明白的。你比那寡妇的小儿子还不如呢!就算我死 
	了，还有我的儿子，我的孙子，我的曾孙子，他们一直傅下去。而这二山是不会加大的，总有 
	一天，我们曾把它何铲平。」 
	智叟听了，无话可说: 
	二山的守镬神被愚公的坚毅精神吓倒，便把此事奏知天帝。天帝佩服愚公的精神，就命两位大 
	力神背走二山。

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


try :
    import stats_word
except :
	print('stats_word.py模块不在当前目录,程序出错退出')
	exit()

#####################
# 以下为测试程序
#####################
print('\n\n以下采用错误数据测试')
text_num=123456789

# 分别采用错误数据测试
print('测试stats_text =========')
print(stats_word.stats_text(text_num))
print('测试stats_text_en =========')
print(stats_word.stats_text_en(text_num))
print('测试stats_text_cn =========')
print(stats_word.stats_text_cn(text_num))

print('\n\n以下采用正确数据测试')
text_chr=' 严雨 and 风随心动 自学学习很有成就感 is very good'

# 分别采用正确数据测试
print('stats_text==========')
print('测试stats_text =========')
print(stats_word.stats_text(text_chr))
print('测试stats_text_en =========')
print(stats_word.stats_text_en(text_chr))
print('测试stats_text_cn =========')
print(stats_word.stats_text_cn(text_chr))

#####################################
print ('\n\n=======以下为英文单词和中文汉字出现次数的输出结果===================\n\n')
word_num_all=stats_word.stats_text( text )
print (word_num_all)



