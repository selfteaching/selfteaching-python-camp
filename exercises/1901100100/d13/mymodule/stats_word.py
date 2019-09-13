# This program is used to take english words or chinese words from a string. and make a 
# statistics. display the result with a descending order
#
#####################################
# -*- coding: uft-8 -*-
from collections import Counter
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
'''

    
def stats_text_cn(text,num):
    # if text is not a string ,then raise a ValueError
    if type(text) != str:
        raise ValueError("you should give a string!")
    # this is the function of statistic the chinese words which are more than two words
    words_ch = jieba.cut(text)
    words_list = []
    for word in words_ch:
        if len(word) > 1:
            words_list.append(word)
    return Counter(words_list).most_common(num)
    

    
if __name__ == '__main__':
    result_all = stats_text_cn(text,15)
    print(result_all)
  #  text_ch = stats_text_cn(text)
  #  print(text_ch)






