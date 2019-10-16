def stats_text_en(text):# 统计英文单词出现的次数
    """Return a list containing English word's counts in decrease."""# 使用文档字符串说明
    import re
    t1=text.lower() #将text lower
    t2=[]
    pttn = r'[a-z]\w+'
    t2=re.findall(pttn, t1)
    d1={} #define dict
    for i in t2:
        d1.setdefault(i,t2.count(i))  #将单词及单词的出现次数，分别赋值给d1的KEY和vaule
      #print(d1)
    d2 = sorted(d1.items(),key = lambda items:items[1],reverse = True)
     #print(d2)
    return d2 #返回统计结果，出现次数从大到小降序输出

def stats_text_cn(text):  # 统计每个中文字出现的次数
    """Return a list containing chinese word's counts in in decrease """  # 使用文档字符串说明
    t1=text
    d1={}
    for i in t1:
        if u'\u4e00' <= i <= u'\u9fff':  #调用中文正则表达式
            d1.setdefault(i,t1.count(i))
    #print(d1)  
    d3 = sorted(d1.items(), key=lambda item: item[1], reverse=True)  #将d1按照value值从大到小降序排列
    return d3 #返回统计结果，次数从大到小降序输出
    

text = '''
愚公移⼭山
太⾏行行，王屋⼆二⼭山的北北⾯面，住了了⼀一個九⼗十歲的⽼老老翁，名叫愚公。⼆二⼭山佔地廣闊，擋住去路路，使他
和家⼈人往來來極為不不便便。
⼀一天，愚公召集家⼈人說:「讓我們各盡其⼒力力，剷平⼆二⼭山，開條道路路，直通豫州，你們認為怎
樣?」
⼤大家都異異⼝口同聲贊成，只有他的妻⼦子表示懷疑，並說:「你連開鑿⼀一個⼩小丘的⼒力力量量都沒有，怎
可能剷平太⾏行行、王屋⼆二⼭山呢?況且，鑿出的⼟土⽯石⼜又丟到哪裏去呢?」
⼤大家都熱烈烈地說:「把⼟土⽯石丟進渤海海裏。」
於是愚公就和兒孫，⼀一起開挖⼟土，把⼟土⽯石搬運到渤海海去。
愚公的鄰居是個寡婦，有個兒⼦子⼋八歲也興致勃勃地⾛走來來幫忙。
寒來來暑往，他們要⼀一年年才能往返渤海海⼀一次。
住在⿈黃河河畔的智叟，看⾒見見他們這樣⾟辛苦，取笑愚公說:「你不不是很愚蠢嗎?你已⼀一把年年紀
了了，就是⽤用盡你的氣⼒力力，也不不能挖去⼭山的⼀一⻆角呢?」
愚公歎息道:「你有這樣的成⾒見見，是不不會明⽩白的。你⽐比那寡婦的⼩小兒⼦子還不不如呢!就算我死
了了，還有我的兒⼦子，我的孫⼦子，我的曾孫⼦子，他們⼀一直傳下去。⽽而這⼆二⼭山是不不會加⼤大的，總有
⼀一天，我們會把它們剷平。」
智叟聽了了，無話可說:
⼆二⼭山的守護神被愚公的堅毅精神嚇倒，便便把此事奏知天帝。天帝佩服愚公的精神，就命兩位⼤大
⼒力力神揹⾛走⼆二⼭山。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.
  
25  Stretching over a wide expanse of land, the mountains blocked
    yugong’s way making it inconvenient for him and his family to get
    around.
26  One day yugong gathered his family together and said,”Let’s do our
    best to level these two mountains. We shall open a road that leads
    to Yuzhou. What do you think?”
27
28  All but his wife agreed with him.
29  “You don’t have the strength to cut even a small mound,” muttered
    his wife. “How on earth do you suppose you can level Mount Taixin
    and Mount Wanwu? Moreover, where will all the earth and rubble go?”
30  “Dump them into the Sea of Bohai!” said everyone.
31
32  So Yugong, his sons, and his grandsons started to break up rocks and
    remove the earth. They transported the earth and rubble to the Sea
of Bohai.
33
34  Now Yugong’s neighbour was a widow who had an only child eight years
    old. Evening the young boy offered his help eagerly.
35
36  Summer went by and winter came. It took Yugong and his crew a full
    year to travel back and forth once.
37
38  On the bank of the Yellow River dwelled an old man much respected
    for his wisdom. When he saw their back-breaking labour, he ridiculed
    Yugong saying,”Aren’t you foolish, my friend? You are very old now,
    and with whatever remains of your waning strength, you won’t be able
    to remove even a corner of the mountain.”
39
40  Yugong uttered a sigh and said,”A biased person like you will never
    understand. You can’t even compare with the widow’s little boy!”
41
42  “Even if I were dead, there will still be my children, my
    grandchildren, my great grandchildren, my great great grandchildren.
    They descendants will go on forever. But these mountains will not
    grow any taler. We shall level them one day!” he declared with
    confidence.
43
44  The wise old man was totally silenced.
45  When the guardian gods of the mountains saw how determined Yugong
    and his crew were, they were struck with fear and reported the
    incident to the Emperor of Heavens.
46
47  Filled with admiration for Yugong, the Emperor of Heavens ordered
    two mighty gods to carry the mountains away.
48  '''

def stats_text(text): 
    """Return a list containing english and chinese word's counts in in decrease """ # 使用文档字符串说明 
    d3=[]
    d3=stats_text_cn(text)+stats_text_en(text) # 分别调用英文和中文统计结果 
    #print(d3)
    return d3 #返回统计结果

        