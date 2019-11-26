# 定义text这个字符串

# 1. 封装统计英⽂文单词词频的函数
# 定义一个名为 stats_text_en 的函数，函数接受一个字符串 text 作为参数
text='''
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
print()
def stats_text_en(text):
# 为 stats_text_en 添加注释说明
    """
    这是一个统计样本text中各个英文单词出现次数的函数
    """
# 实现该函数的功能（同 day5 任务 2）：统计参数中每个英⽂文单词出现的次数，最后返回一个按词频降序排列的数组
# 使⽤用字典（dict）统计字符串串样本 text 中各个英⽂文单词出现的次数。
elements = text.split()
words = []
symbols= ',.*-!'
for element in elements:
    for symbol in symbols:
        element = element.replace(symbol,'')
    if len(element):
        words.append(element)
print('正常的英文单词 ==>',words)
print()
print()
counter = {}
word_set = set(words)
for word in word_set:
    counter[word] = words.count(word)
print("英文单词出现的次数 ==>",counter)
print()
print()
print('从大到小输出所有的单词及出现的次数 ==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))
print()
print()
print()
help(stats_text_en)
print()

# 2. 封装统计中⽂文汉字字频的函数
text='''
愚公移⼭
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
'''
def stats_text_cn(text):
    """
    这是一个统计样本text中各个中文汉字出现次数的函数
    """
elements = text.split()
words = [] # 这里的word是汉字
symbols= '。，；' # 这里的symbols是标点符号
for element in elements:

    # 统计以及删除标点符号symbols
    for symbol in symbols:
        element = element.replace(symbol,'')
    ## 之前一直缺一行这样的代码，即保留输出words中所有的重复性汉字
    for word in element:
        words.append(word)

    # 统计并保留汉字word
    for word in range(0,len(element)):
        # 如果字符第一次出现 加入到字符数组中
        if not element[word] in words:
            words.append(element[word])
        # 如果是字符第一次出现 加入到字典中
        elif element[word] not in counter:
            counter[element[word]] = 1

print('正常的中文汉字 ==>',words)
print()
print()
counter = {}
word_set = set(words)
for word in word_set:
    counter[word] = words.count(word)
print("中文汉字出现的次数 ==>",counter)
print()
print()
print('从大到小输出所有的汉字及出现的次数 ==>', sorted(counter.items(), key=lambda x: x[1], reverse=True))
print()
print()
print()
help(stats_text_cn)
print()

def stats_text(text):
    """这是一个统计样本text中各个中文汉字/英文字母出现次数的函数."""   
    return stats_text_en(text) + stats_text_cn(text) 
help(stats_text)
print()

