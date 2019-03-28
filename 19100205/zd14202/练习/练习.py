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
How The Foolish Old Man Moved Mountain
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
# 函数1：统计输入文本中英文单词的词频： 
def stats_text_en(text): 
    text = text.replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace(',', '').replace('(', '').replace(')', '').replace(';', '').replace(':', '').replace('\'', '').replace('?', '').replace('_', '').replace('-', '').replace('/', '') .replace('[', '') .replace(']', '') .replace('\\', '') .replace('\"', '').replace('{', '').replace('}', '').replace('\t', '').replace('\n', '').replace('\r\n', '')     
    # 去除标点符号 
    textlist = [] # 将字符串转换为列表 
    a = {} 
    for i in list_text: 
        a[i] = list_text.count(i)
    a = sorted(a.items(),key = lambda x:x[1],reverse = True) 
    return a 
# 函数2：统计中文词频： 
def stats_text_cn(text):   
    b = {}
    for i in text:  # 这个循环有效，说明一串汉字也是一个字符串，每个汉字就是其中的一个元素，可以用for in 来遍历，其中i代表了每个汉字的unicode编码 
        if u'\u4e00' <= i <= u'\u9fff':     # 挑选出中文字 
            b[i] = text.count(i)      # 用.count()函数/方法来对每个元素（这里是汉字）进行计数，形成一个列表 
    b = sorted(b.items(), key=lambda x: x[1], reverse=True)  #按出现数字从大到小排列 
    return b 
# 函数3：统计中英文混合词频： 
def stats_text(text): 
    '''函数说明： 
    本函数的功能是统计输入文本的汉字及英语单词词频，并以降序排列输出。''' 
    dic_1 = stats_text_cn(text) # 调用函数1统计中文字词频 
    for i in text: 
        if u'\u4e00' <= i <= u'\u9fff': 
            text = text.replace(i,"") #删除所有中文字 
    text = text.replace('「', '').replace('」', '').replace('，', '').replace('。', '').replace('：', '').replace('？', '').replace('！', '') 
    # 以上一句删除所有中文标点 
    dic_2 = stats_text_en(text) # 调用2函数统计英文单词词频  
    dic_3 = {} 
    dic_3.update(dic_2) 
    dic_3.update(dic_1) # 将之前分别得到的两个中英文词频结果字典合并 
    dic_3 = sorted(dic_3.items(),key = lambda x:x[1],reverse = True) # 对合并后的字典进行排序，得出混合排序结果 
    return(dic_3) 
# print(stats_text(text)) 
print(stats_text.__doc__)  