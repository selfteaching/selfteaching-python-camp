# text = '''
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambxiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# '''

# #该函数的功能是将带有“,.*-!?""”标点符号的英文单词字符串中的单词进行单词出现个数统计，
# #最后返回一个按词频降序排列的数组
# def stats_text_en(str):
#     #将文档中的大小写全部换为小写
#     str=str.lower()
#     #将文档中的标点符号，全部换为空
#     biaodian=',.*-!?"":'
#     for i in biaodian:
#         str=str.replace(i,'')
#     #将字符串转换为单词列表
#     str=str.split()
#     #开始统计单词列表中单词个数
#     str_dict={}
    
#     for char in str:
#         if char in str_dict:
#             count=str_dict[char]
#         else:
#             count=0
#         count +=1
#         str_dict[char]=count
#     #循环结束后，会生成一个单词及单词个数的字典，这时的字典没有排序
#     #下面对字典进行排序
#     char_dict=sorted(str_dict.items(),key=lambda x:x[1],reverse=True)
    
#     print(char_dict)#输出排序后的字典
    
# stats_text_en(text)

# text = '''
# 二跳强弱：
# 1.最强青蛙跳：①涨停板（第二天没大幅低开）②突破缺口伴随创新高（最好不带上影线、大阴线）。
# 2.强势青蛙跳：大阳线（7%）
# 3.普通青蛙跳：新高附近，没大阳线，能明显看出来二跳。
# 4.风险青蛙跳：二跳上影线、二跳大阴线、二跳距离前期高点很远、二跳缠绵，二跳的时间比一踩二踩都长。
# 快速回到前期高点附近，几根大阳线就完成反弹，和前高差距上下10%以内
# 回踩强弱：
# 1.横盘是最强的回踩。
# 2.二踩比一踩重要（最好是二踩跌幅变小、阴线变少）。
# 3.一踩二踩出现大阴线、上影线，不代表不能走出主升浪，需要结合一跳二跳分析,综合分析整体的风险和机会比。
# （大阴线和上影线在二跳中出现，比在一踩二踩中出现，对于风险提示的意义更大！）。
# 日线级别一踩跌幅不能超过一跳的50%，二踩不能超过一跳的30%，所用时间（K线数量）不能少于二跳，阴线占比不能超过50%。
# 一跳强弱：
# 1.日线级别一跳普遍都带有涨停板，只有少数不带。
# 2.一跳最好有较多的实体阳线，而不是一字板直接上去的，当然新股除外。
# 3.涨幅太大的情况（一跳涨幅在一倍以上），不管是一字板还是阳线构成的，都需要谨慎一些。
# 4.一跳高点的大阴线、上影线，对于青蛙跳整体走势的影响，就和一踩二踩一样，并不是那么关键，如果同时（一跳和一踩二踩），出现了弱势情况，那么我们才需要多加谨慎。


# 四、实战操作
# 标准买点的核心：
# 在时间和空间大体相似的情况下，成交量持续的极度缩量！
# 缩量幅度起码比二跳高点减少一半以上，最好比一踩的最低成交量还要低！
# 一踩二踩的底部最好是非常低的量，二跳最高点的成交量要在一跳最高点量的0.5-1.5倍之间，突破时成交量越大越好。
# '''

# #该函数用于统计字符串中每个汉字出现的个数。需要输入字符串，输出的结果是按照降序排列的以中文汉字及其字频为元组的一个字典
# def stats_text_cn(str):
#     #移除字符串头尾的空格和换行符号
#     str=str.strip()
#     #去除所有的标点符号
#     biaodian='。，“”…，——，？：、！《》'
#     for i in biaodian:
#         str=str.replace(i,'')
#     #目前字符串str中应该只包含汉字，下面对汉字字符串进行统计
#     #方法与统计单词基本一样，因为这里是统计中文汉字个数，所以每个汉字都是一个元素，
#     #于是没有必要去将字符串再转换成一个单词列表
#     char_dict={}
#     for char in str:
#         if char in char_dict:
#             count=char_dict[char]
#         else:
#             count=0
#         count +=1
#         char_dict[char]=count
#     char_dict=sorted(char_dict.items(),key=lambda x:x[1],reverse=True)
#     #输出最后的结果
#     print(char_dict)

# stats_text_cn(text)

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

import collections
import re

def stats_text_en(string_en):

    result = re.sub("[^A-Za-z]", " ", string_en.strip())
    newList = result.split( )
    print('英文单词词频统计结果： ',collections.Counter(newList),'\n')
    

def stats_text_cn(string_cn):
    result1 = re.findall('[\u4e00-\u9fff]+', string_cn)
    newString = ''.join(result1)
    print('中文单词词频统计结果： ',collections.Counter(newString),'\n')


# 调用函数
# stats_text_en(text)
# stats_text_cn(text)

def stats_text(text):  # 合并中英文词频统计, 如何调用两个函数 【原来就是两个函数相加这么简单。】

        """combine the stats_text_cn and stats_text_en,count english words and chinese characters"""

        a = stats_text_en(text)

        b = stats_text_cn(text)

        c = a+b

stats_text(text)

# import stats_word

