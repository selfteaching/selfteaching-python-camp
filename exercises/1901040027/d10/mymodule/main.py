text2 = '''
愚公移山

太行、王屋二山，方七百里，高万仞，本在冀州之南，河阳之北。

北山愚公者，年且九十，面山而居。惩山北之塞，出入之迂也，
聚室而谋曰：“吾与汝毕力平险，指通豫南，达于汉阴，可乎？”杂然相许。
其妻献疑曰：“以君之力，曾不能损魁父之丘，如太行、王屋何？且焉置土石？”杂曰：“投诸渤海之尾，隐土之北。”遂率子孙荷担者三夫，叩石垦壤，箕畚运于渤海之尾。邻人京城氏之孀妻有遗男，始龀，跳往助之。寒暑易节，始一返焉。
河曲智叟笑而止之曰：“甚矣，汝之不惠！
以残年余力，曾不能毁山之一毛，其如土石何？”北山愚公长息曰：“汝心之固，固不可彻，曾不若孀妻弱子。
虽我之死，有子存焉；子又生孙，孙又生子；子又有子，子又有孙；子子孙孙无穷匮也，而山不加增，何苦而不平？”河曲智叟亡以应。
操蛇之神闻之，惧其不已也，告之于帝。帝感其诚，命夸娥氏二子负二山，一厝朔东，一厝雍南。自此，冀之南，汉之阴，无陇断焉。

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

import stats_word
#test = 3.1415926 #用于 try except 捕获异常并执行
#try:
stats_word.stats_text(text2, 50)
#except ValueError:
 #   print('Input is not str,you may check again!')

#try:
#stats_word.stats_text_en(text2, 7)
#except ValueError:
    #print('Input is not str,you may check again!')


import stats_word
import json
import jieba
with open('tang300.json','r', encoding = 'utf-8') as f:
    temp = json.loads(f.read())
str = json.dumps(temp, ensure_ascii=False)
f.close()
#str1 = str.replace('"','').replace('n','').replace('t','').replace(':','').replace(',','').replace('。','').replace('','').replace('\\','').replace('e','').replace('n','').replace('t','').replace('{','')
#处理字符串中的英文字母，标点符号有哪些更便捷的方法？
int_num = 20
t_300 = stats_word.stats_text_cn(str, int_num)
print(t_300)