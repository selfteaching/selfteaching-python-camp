text = '''
 愚公移山 
 太行，王屋二山的北面，住了一個九十歲的老翁，名叫愚公。二山佔地廣園，檔住去路，使他 和家入往來極為不便。 ’ 
 一天，愚公召集家人說：「讓我們各盡其力，刻平二山，開條道路，直通豫州，你們認為怎 樣？ j 
 大家都異口同聲贊成，只有他的妻子表示懷疑，並說：「你連開脇一個小丘的力量都沒有，怎 可能翻平太行、王屋二山呢？況且，磐出的土石又丢到哪裏去昵？ J 
 大家都熱烈地說： 「把土石丢進激海裏。」 
 於是愚公就和兒孫，一起開挖土， 把土石搬運到激海去。 
 愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地走來黎忙。 
 寒来書往，他們要一年才能往返激海一次。 
 住在黃河河畔的智叟，看見他1們這樣辛苦，取笑愚公說：「你不是很愚意嗎？你已一把年紀 了. 就是用盡你的氣力，也不能挖去山的一角呢？」 
 愚公歎息道： 「你有這樣的成見，是不會明白的。你比那寡婦的小兒子進不如呢！ 就算我死 了， 進有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有 一天，我們會把它們劇平。」 
 智叟聽了 ， 無話可說： 
 二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大 力神措走二山。
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
 mighty gods to carry the mountains away.'''

import stats_word
print(stats_word.stats_text(text))
 
dict1 = {} #设立数据容器
dict2 = {}
dict3 = {}
dict4 = {}

def stats_text_en(text):  #设定函数 
import re #引入系统函数
text = re.sub("[^A-Za-z]", " ", text.strip())  #只留英语单词
list1 = re.split(r"\W+",text)   #把单词存入一个list里

while '' in list1:   
         list1.remove('')  #删除空格

    for i in list1:   

          dict1.setdefault(i,list1.count(i))  #把单词极其频次统计到一个字典里

      tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)   #按照字频排序 

      for tup1 in tup1:   
             dict2[tup1[0]] = dict1[tup1[0]]  
     return dict2#组装到新字典中

 
      print(stats_text_en(text))#打印出英文词频

 
def histogram(s, old_d):#设置一个更新数量的函数
     d = old_d
     for c in s:
         d[c] = d.get(c, 0) + 1
     return d

def stats_text_cn(text): #只针对汉字的函数
     import re
     text = re.sub("[A-Za-z0-9]", "", text) #遴选出汉字

      list1 = re.split(r"\W+",text)   #分割汉字

      while '' in list1:   
         list1.remove('') #去除空格

      dict3 = dict()        #use dict function

      for i in range(len(list1)):
         dict3 = histogram(list1[i], dict3)

 
      tup1 = sorted(dict3.items(),key = lambda items:items[1],reverse = True)  

      for tup1 in tup1:   
             dict4[tup1[0]] = dict3[tup1[0]]  
     return dict4

  #print(stats_text_cn(text))#统计汉字

 
  def stats_text(text):
     return dict(stats_text_en(text),**stats_text_cn(text))

 
