from inspect import signature
from functools import wraps
from collections import Counter
import re

def typeassert(*type_args, **type_kwargs):
    def decorate(func):
        sig = signature(func)
        bound_types = sig.bind_partial(*type_args, **type_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise ValueError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(str)
def stats_text_en(text):
    """统计参数中每个英文单词出现的次数，最后返还一个按词频降序排列的数组"""
    textlist1 = text.split()#形成单词列表
    textlist2 = []
    for i in textlist1:
        if i.isalpha():
            textlist2.append(i)#去除非单词
    '''
    dict1 = {}
    dict1 = dict1.fromkeys(textlist2)#将textlist2的元素作为dict1的键值key
    word_1 = list(dict1.keys())
    for i in word_1:
        dict1[i] = textlist2.count(i)#统计单词出现的次数
    dict2 = {}
    dict2 = sorted(dict1.items(),key=lambda d:d[1],reverse=True)#按values进行排序
    dict2 = dict(dict2)#转化为字典
    print(dict2)#输出字典
    '''
    count = input('输出个数')
    count = int(count)
    print(Counter(textlist2).most_common(count))


@typeassert(str)
def stats_text_cn(text):
    #统计参数中每个中文汉字出现的次数，最后返10回一个按字频降序排列的数组
    dict1 = {}
    for i in text:
        if i in ['」','「','!','-','’',' ','/n',',','，','.','，','。','”','“','※','…','？','：','！','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            continue
        if i not in dict1:        #为首次出现的字创建key
            dict1[i] = 0
        dict1[i] += 1
    '''dict1 = sorted(dict1.items(),key=lambda item:item[1],reverse=True)          #创建以键值对为元素的元组
    list1 = []
    for j in range(len(dict1)):
        list1.append(dict1[j][1])
    print(list1)            #返回按字频降序排列的数组
    '''
    count = input('输出个数')
    count = int(count)
    print(Counter(dict1).most_common(count))
 
@typeassert(str)
def stats_text(text):
    """输出合并词频统计结果"""
    stats_text_en(text)
    stats_text_cn(text)



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

stats_text_en(text)
stats_text_cn(text)