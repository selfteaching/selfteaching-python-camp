text = '''
化肥会挥发,黑化肥发灰,灰化肥发黑.黑化肥发灰会挥发 化发化黑
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
#去除符号
a=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
#print (a)
a=a.split() # 切割字符串  
#print(a)
def stats_text_en(a):   #定义函数
    import collections  #引用collections包

    if type(a) != str:                   #利用判断语句进行分析
        raise ValueError('valuerror:it is not string stats_text_en')

    c=collections.Counter(a)  #Counter 确定次数
    return c            #返回值

#print(stats_text_en(a))  使用函数


def stats_text_cn(x): #定义函数
    j={}

    if type(x)!=str:                   #利用判断语句进行分析
        raise ValueError('valuerrorr:it is not string stats_text_en')

    for i in x :                    #通过循环统计汉字
        if '\u4e00' <= i <= '\u9fff' :
            j[i]=x.count(i)+1
        else:
            j[i]=x.count(i)
    text3=j.items()                  #字典函数
    text4=sorted(text3,key=lambda i:i[1],reverse=True)#降序
    return (text4)

def stats_text(a):

    if type(a) !=str:                   #利用判断语句进行分析
        raise ValueError('valuerror:it is not string stats_text_en')

    return stats_text_en(a) ,stats_text_cn(a)



    