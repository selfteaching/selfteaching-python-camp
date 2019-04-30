import re
import collections
import jieba
import string

#英文和中文字符匹配规则
en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
cn_pattern = re.compile(r'[\u4e00-\u9fa5]')

#字符串示例
template =  '''

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
Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。
'''


#检验是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

#创建一个名为stats_text_en的函数，封装day5中任务2的代码到刚这个函数下，同时用文档字符串为stats_text_en添加注释说明
def stats_text_en(text,count=None):
    ''' 
    以字典形式返回字符串中英文单词的出现频率
    :param text:string 输入的字符串
    :param count:int 控制输出个数
    :return list:英文单词词频统计结果(列表形式输出)
    '''
    # 在这里写具体操作
    mydict=[]
    mylist=[]
    try:
        mylist=re.findall(en_pattern,text)
    except ValueError:
        print("stats_text_en(ValueError):please input string")
    except TypeError:
        print("stats_text_en(TypeError):please input string")
    # #实现英文单词词频统计的模块（old）
    # for mylinum in mylist:
    #     if mylinum in mydict:
    #         mydict[mylinum]=int(mydict[mylinum])+1
    #     else:
    #         mydict[mylinum]=1
    #实现英文单词词频统计的模块（new），用python自带的Counter函数
    mydict=collections.Counter(mylist).most_common(count)

    return mydict
#print(sorted(stats_text_en(template).items(), key=lambda d: d[1],reverse=True))

#创建一个名为stats_text_cn的函数，该函数的功能是实现统计每个中文汉字出现的次数，同时用文档字符串添加注释说明
def stats_text_cn(text,count=None):
    ''' 
    以字典形式返回字符串中文汉字的出现频率
    :param text:string 输入的字符串
    :param count:int 控制输出个数
    :return list:中文汉字词频统计结果（列表形式输出）
    '''
    # 在这里写具体操作
    mydict=[]
    mylist=[]
    mylisttemp=[]
    try:
        #mylist=re.findall(cn_pattern,text)

        non_word_char = '＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏。？'
        non_word_char += string.punctuation + string.whitespace
        trans = str.maketrans({key: None for key in non_word_char})
        text = text.translate(trans)

        mylist=jieba.lcut(text,cut_all=False)
        for mylistitem in mylist:
            #if is_all_chinese(mylistitem)==True and len(mylistitem)>=2:
            if len(mylistitem)>=2:
                mylisttemp.append(mylistitem)

    except ValueError:
        print("stats_text_cn(ValueError):please input string")
    except TypeError:
        print("stats_text_cn(TypeError):please input string")
    # #实现英文单词词频统计的模块（old）
    # for mylinum in mylist:
    #     if mylinum in mydict:
    #         mydict[mylinum]=int(mydict[mylinum])+1
    #     else:
    #         mydict[mylinum]=1
    #实现英文单词词频统计的模块（new），用python自带的Counter函数
    mydict=collections.Counter(mylisttemp).most_common(count)

    return mydict
#print(sorted(stats_text_cn(template).items(), key=lambda d: d[1],reverse=True))

#创建一个名为stats_text的函数，该函数的功能是实现统计字符串中英文单词和中文汉字的词频
def stats_text(text,rmodel,count=None):
    '''
    统计一段字符串中中文和英文的词频
    :param text:string 输入的字符串
    :param rmode:int 读取类型 1:中文 2:英文 0:中英混合
    :param count:int 控制输出个数
    :return list:中文和英文单词词频统计结果（列表形式输出）
    '''
    mylist_en=[]
    mylist_en=re.findall(en_pattern,text)
    mylist_cn=[]
    mylist_cn=re.findall(cn_pattern,text)
    dicttmp=[]
    try:
        if rmodel==1:
            dicttmp=collections.Counter(mylist_cn).most_common(count)
        elif rmodel==2:
            dicttmp=collections.Counter(mylist_en).most_common(count)
        else:
            dicttmp=collections.Counter(mylist_en+mylist_cn).most_common(count)
    except ValueError:
        print("stats_text(ValueError):please input string")
    except TypeError:
        print("stats_text(TypeError):please input string")
    return dicttmp


def main():
    mdict=[]
    mdict=stats_text_cn(template,10)
    print(mdict)


if __name__ == '__main__':
    main()

