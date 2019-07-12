text = '''
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

def stats_text_en(text):
    #定义英文单词按词频降序排列的函数
    if type(text) == str:
        dictionary={} 
        #创建一个字典
        text_en=text.replace(',',' ').replace('.',' ').replace('?”',' ').replace('!',' ').replace(',"',' ')
        #将text中标点符号用空格替换
        mytext=text_en.split( ) 
        for i in mytext:                
            dictionary[i]=mytext.count(i) 
        dic=sorted(dictionary.items(),key=lambda item:item[1],reverse=True)
        #按照值从大到小的排序
        print(dic)
        #返回一个按词频降序排列的数组
    else:
        raise ValueError('参数必须是str类型')

text1='''愚公移⼭山
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
⼒力力神揹⾛走⼆二⼭山。'''

def stats_text_cn(text1):
    #定义中文按字频降序排列的函数
    if type(text1) == str:
        dictionary={} 
        #创建一个字典
        text_cn=text1.replace('，','').replace('！','').replace('：','').replace('」','').replace('。','').replace('「','').replace('？','').replace('、','').replace(' ','').replace('\n','')
        #将text中标点符号替换为空
        for i in text_cn:                
            dictionary[i]=text_cn.count(i) 
        dic=sorted(dictionary.items(),key=lambda item:item[1],reverse=True)
        #按照值从大到小的排序
        print(dic)
        #返回一个按字频降序排列的数组
    else:
        raise ValueError('参数必须是str类型')

def stats_text():
    return(stats_text_en(text)+stats_text_cn(text1))

stats_text()


