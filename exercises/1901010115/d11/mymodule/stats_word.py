import re
from collections import Counter
import json #测试用
with open('tang300.json',mode='r',encoding='utf-8') as f: #测试用
    read_data = f.read() #测试用
import jieba


text = '''
愚公移⼭
太⾏，王屋⼆⼭的北⾯，住了⼀個九⼗歲的⽼翁，名叫愚公。⼆⼭佔地廣闊，擋住去路，使他
和家⼈往來極為不便。
⼀天，愚公召集家⼈說：「讓我們各盡其⼒，剷平⼆⼭，開條道路，直通豫州，你們認為怎
樣？」
⼤家都異⼝同聲贊成，只有他的妻⼦表示懷疑，並說：「你連開鑿⼀個⼩丘的⼒量都沒有，怎
可能剷平太⾏、王屋⼆⼭呢？況且，鑿出的⼟⽯⼜丟到哪裏去呢？」
⼤家都熱烈地說：「把⼟⽯丟進渤海裏。」
於是愚公就和兒孫，⼀起開挖⼟，把⼟⽯搬運到渤海去。
愚公的鄰居是個寡婦，有個兒⼦⼋歲也興致勃勃地⾛來幫忙。
寒來暑往，他們要⼀年才能往返渤海⼀次。
住在⿈河河畔的智叟，看⾒他們這樣⾟苦，取笑愚公說：「你不是很愚蠢嗎？你已⼀把年紀
了，就是⽤盡你的氣⼒，也不能挖去⼭的⼀⻆呢？」
愚公歎息道：「你有這樣的成⾒，是不會明⽩的。你⽐那寡婦的⼩兒⼦還不如呢！就算我死
了，還有我的兒⼦，我的孫⼦，我的曾孫⼦，他們⼀直傳下去。⽽這⼆⼭是不會加⼤的，總有
⼀天，我們會把它們剷平。」
智叟聽了，無話可說：
⼆⼭的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位⼤
⼒神揹⾛⼆⼭。
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

text1 = '''
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

text2 = '''
/“/请/！/”/“/请/！/”/两名/剑士/各自/倒转/剑尖/，/右手/握/剑柄/，
/左手/搭于/右手/手背/，/躬身行礼/。/两/人/身子/尚未/站/直/，
/突然/间/白光闪/动/，/跟着/铮的/一/声响/，
/双剑相/交/，/两/人/各/退一步/。
/旁/观众/人/都/是/“/咦/”/的/一声/轻呼/。/青衣/剑士/连/劈/三/剑/
'''

text3 = '''
二 结构化思维，几乎是最值得刻意训练的能力！
然而在现实中，很多人往往忽略结构化思维的培养，因为他们认为，这是天生的。他们要么觉得自己足够聪明所以不需要培养，要么觉得我天生不聪明，学不来，干脆放弃。
我曾经在文章中提到过能力的重要性。有人问，能力有那么多，到底培养哪一个才好呢？如果我用一个两维矩阵来分析的话，可以看到，结构化思维能力，是既能够被培养同时价值度又高的能力。
'''

def stats_text_en(t,count): #定义函数，参数为t
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        t = t.lower() #文本转小写
        t = re.sub(r'[^A-Za-z]',' ',t)
        t_list = t.split() #文本转列表
        x = Counter() #设定一个空计数器
        for i in t_list: #指定i遍历上述列表
            ii = i.strip(' ,.*!-') #清洗i中元素
            x[ii] += 1 #计数清洗完的单词
        return x.most_common(count)#得单词计数结果（已自动排序）

def stats_text_cn(t,count): #定义函数，参数为t
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        t_list = [] #新建一个空列表
        exclude_str = '\n ，。！？/”“「」:\',[]' #新建一个字符串,备用（将要消除的中文符号）
        y = Counter()
        for char in t: #遍历文本中的字节
            t_list.append(char) #把拆解的所有字节（包括单个汉字和符号）放入新建的列表中
        for char in t_list: #遍历列表中的元素
            if '\u4e00'<=char<='\u9fff':#如果该字节为汉字，不是符号
                y[char.strip()] += 1
        return y.most_common(count)

def stats_text(t,count):
    if not isinstance(t,str): #如果t不是字符串
        raise ValueError('wrong operand type') #则报错
    else: #如果t是字符串
        stats_text_en(t,count)
        stats_text_cn(t,count)
        return (print(stats_text_en(t,count) + stats_text_cn(t,count)))

def cn(t,count):
    b = [i for i in t if '\u4e00' <= i <= '\u9fa5'] #去除汉字以外的i，合并为列表b
    str_b = ''.join([str(i) for i in b]) #把列表b转化为无间距字符串str_b
    list_b = jieba.lcut(str_b,cut_all=False) #用词库jieba分词字符串str_b后的列表,list_b
    z = Counter()
    for j in list_b: #j为列表list_b中一个词
        if len(j)>=2: #如果单个词的汉字数大于等于2
            z[j] +=1 #则汉字数大于等于2的词整合为一个词典，并计数排列
    return z.most_common(count)
