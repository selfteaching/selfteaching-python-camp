text ='''
愚公移山的故事

太行和王屋两座大山，方圆七百里，高达几万尺，原来位于冀州的南面，河阳的北面。

　　山北有位老人，叫做愚公，年纪快九十了。他家的住处正对着这两座大山。他苦于大山阻隔，出入的道路十分迂曲艰难，就召集全家人商议说：“我想和你们一起，用尽一切力量去搬掉这险阻，开出一条大路，直通冀州的南部，到达汉水的南面，你们说行吗？”

　　全家人纷纷表示赞同。只有他的妻子提出一个疑问，说：“就凭你这点力气，就是像魁父这样的小山包，恐怕都搬不掉，又能把太行、王屋这两座大山怎么样呢？再说，挖出来的那些石头和泥土又往哪里扔呢？”

　　家人七嘴八舌地说：“把它们扔到渤海的边上，隐土的北面去。”

　　于是，愚公就率领着三个能挑担子的子孙，凿石头，挖土块，再用簸箕和筐子把石土运到渤海的后面去。就这样从冬到夏，他们才能往返一次。

　　愚公家搬山的事，惊动了邻居。邻居家的一位寡妇，有个遗腹子，才刚七八岁，也蹦蹦跳跳跑去帮忙。

　　黄河边上住着一个老头，人称智叟。他以嘲笑的语气劝阻愚公说：“你怎么傻到这种地步呀！就凭你这把年纪，这点儿力气，要拔掉山上的一根树都不容易办到，又怎么能搬掉这么多的山石土块呢？”

　　愚公长叹了一口气，说：“我看你太顽固了，简直不明事理，连那寡妇的小孩都不如！虽然我会死的，可是我还有儿子呢！儿子又生孙子，孙子又生儿子，儿子又生儿子，儿子又生孙子，这样子子孙孙都不会断绝的呀！而这两座山再也不会增高了，还怕挖不平吗？”

　　智叟听了，无言以对。

　　山神听到了愚公的这些话，担心他挖山不止，就去禀告了天帝。天帝为愚公移山的诚意所感动，就派了夸娥氏的两个儿子去背走了那两座大山，一座山放在朔东，一座山放到雍南。从此以后，从冀州的南部，直到汉水的南面，再也没有大山挡路了。

　　愚公移山比喻依靠大家、坚持不懈一定能取得成功。


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
mighty gods to carry the mountains away.


'''

import collections

#import jieba    #jieba第三方库（day10_exercise)（这个位置也可以）

a = text.lower()
a = a.split()  # 指定分隔符对字符串进行切片
a.pop()  # 删除list中的中文元素
found = {}  # 初始化一个词典


def stats_text_en():      # 定义检索中文函数
    """统计参数中每个英文单词出现的次数"""  # 注释
    global text  # 把text标记为全局变量

    if not isinstance(text, str):
        raise ValueError('不是字符串类型(string)!')

   

    for i in a:
        if i in found:
            found[i] += 1
        else:
            found[i] = 0
        found[i] += 1


    print('英文单词词频： ', collections.Counter(found).most_common(1))
    #print('英文单词词频：', sorted(found.items(), key=lambda x: x[1], reverse=True))  # 词频降序


stats_text_en()    # 调用函数

# 统计中文词频


import re

import jieba             #jieba第三方库（day10_exercise)

def stats_text_cn():      # 定义检索英文函数
    """统计参数中每个中文单词出现的次数"""  # 注释
    global text  # 把text标记为全局变量

    

    if not isinstance(text, str):
        raise ValueError('不是字符串类型(string)!')

    
    #text = [x for x in jieba.cut_for_search(text) if len(x) >= 2]  #使用精确模式分词（位置不对）

    found = {}      # 初始化一个词典

    # 提取中文字符串
    text = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", text)
    text = text.replace("  ", '')  # 提取的中文字符串会算上空格，会被统计上，故移除空格

    text = [x for x in jieba.cut_for_search(text) if len(x) >= 2]  #使用精确模式分词(day10_exercise)
    #通过jieba精确模式将stats_word.py中stats_text_cn函数的输入字符串进行分词
    #统计分词完成之后的词频（中文词只统计长度大于等于2的词）

    #print(text)                   #感觉多余

    for i in text:
        if i in found:
            found[i] += 1
        else:
            found[i] = 0
            found[i] += 1

    
    print('中文单词词频： ', collections.Counter(found).most_common(20))
    #print('中文汉字字频： ', sorted(found.items(), key=lambda x: x[1], reverse=True))

stats_text_cn()   # 调用函数

def stats_text(text):
    if not isinstance(text,str):
        raise ValueError('不是字符串类型(string)!')
    stats_text_en(text)
    stats_text_cn(text)

# 以下为调试函数用
# stats_text_en(text)
# stats_text_cn(text)