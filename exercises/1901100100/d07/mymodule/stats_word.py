# This program is used to take english words or chinese words from a string. and make a 
# statistics. display the result with a descending order
#
#####################################
# -*- coding: uft-8 -*-
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


#split the string to list for statistic
def stats_text_en(text):
    #counts the number of text, and return a list ordered by the consquences.
    list_en = text.split()
    words = []
    for j in list_en:
        word = ""
        for i in j:
            if (u'\u0041' <= i <=u'\u005a') or (u'\u0061' <= i <=u'\u007a'):
                word += i
                #delete all the chars which is not letters
        if word != "":
            words.append(word)
    #return result
    
    
    dictionary_1 = {} 
    set_word = set(words)
    #use the dictionary to make the order of the words
    #use dictionanry to count the list1                              
    for word in set_word:
        dictionary_1[word] = words.count(word)
    # get a dictionary with all the words
    templist = sorted(dictionary_1.items(), key=lambda d:d[1], reverse = True )     #sort the dictionary and output a list contains tuples
    # to order the dictionary descendingly
    dictionary_1 = {}                                                               #reset the dictionary
    for i in templist:                                                              #change the list to sorted dictionary
        dictionary_1[i[0]] = i[1]

    #sored_dic = sorted(dictionary_1.items())
    return dictionary_1
    #print(dictionary_1)

def stats_text_cn(text):
    # this is the function of statistic the chinese words
    list_ch = []
    text_ch = ""
    for i in text:
        if u'\u4e00' <= i<=u'\u9fff':
            list_ch.append(i)
    set_words = set(list_ch)
    dic_ch = {}
    for word in set_words:
        dic_ch[word] = text_ch.count(word)
    list_ch = sorted(dic_ch.items(),key = lambda d:d[1],reverse = True)
    dictionary_1 = {}                                                               #reset the dictionary
    for i in list_ch:                                                              #change the list to sorted dictionary
        dictionary_1[i[0]] = i[1]
    return dictionary_1

def stats_text(text):
    #call the two fuctions to statistic the word of a string
    result_en = stats_text_en(text)
    result_ch = stats_text_cn(text)
    result_en.update(result_ch)
    #merge the two dics to one
    list_all = sorted(result_en.items(),key = lambda d:d[1],reverse = True)
    dictionary_1 = {}                                                               #reset the dictionary
    #order the dictionary again
    for i in list_all:                                                              #change the list to sorted dictionary
        dictionary_1[i[0]] = i[1]
    return dictionary_1
    
if __name__ == '__main__':
    result_all = stats_text(text)
    print(result_all)
  #  text_ch = stats_text_cn(text)
  #  print(text_ch)






