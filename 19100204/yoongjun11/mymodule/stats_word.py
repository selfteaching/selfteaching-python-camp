text = '''
愚公移山
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

dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
  
def stats_text_en(text):                           # 定义一个名为stats_text_en的函数
    import re 
    text = re.sub("[^A-Za-z]", " ", text.strip())  # 使用正则表达式"[a-zA-Z]+"，将非英文字母替换成空字符
    list1 = re.split(r"\W+",text)                  # 将字符串text转换为列表list1,只保留单词为list1中的元素
    while '' in list1:                             # 删除list1中为空的列表元素
        list1.remove('')
    for i in list1:                                # i属于list1中的元素，开始循环
        dict1.setdefault(i,list1.count(i))         # 将列表中的单词及单词的出现次数，分别赋值给dict1的键和值
    # 将dict1按照value值倒序排列，并将结果赋给元组tup1
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   
    for tup1 in tup1:   
            dict2[tup1[0]] = dict1[tup1[0]]  
    return dict2

#打印统计英文词频的结果
print("统计英文词频的结果为:")
print(stats_text_en(text))
str = ''

def feng_zhuang(s, old_d):                            # 封装函数
    d = old_d
    print(s,d)
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d
    

def stats_text_cn(text):                             # 定义一个名为stats_text_cn的函数
    import re
    text = re.sub("[A-Za-z0-9]", "", text)           # 使用正则表达式"[A-Za-z0-9]"，将非英文字母替换成空字符
    list1 = re.split(r"\W+",text)                    # 将字符串text转换为列表list1,只保留单词为list1中的元素
    while '' in list1:                               
        list1.remove('')                             # 删除list1中为空的列表元素
    dict3 = dict()                                   # 把dict3的行拆成字典
    for i in range(len(list1)):
        dict3 = feng_zhuang(list1[i], dict3)         # 调用函数，引用传递参数

    # 将dict3按照value值倒序排列，并将结果赋给元组tup1
    tup1 = sorted(dict3.items(),key = lambda items:items[1],reverse = True)  
    for tup1 in tup1:   
            dict4[tup1[0]] = dict3[tup1[0]]  
    return dict4

#打印统计中文词频的结果
print("统计中文词频的结果为:")
print(stats_text_cn(text))

# 调用函数，合并统计英汉词频
def stats_text(tstats_text_en,stats_text_cn):
    if type(text_en_cn) == text:
        return (stats_text_en(text_en_cn,count_en_cn)+stats_text_cn(text_en_cn,count_en_cn))
    else :
        raise ValueError('it is not text')