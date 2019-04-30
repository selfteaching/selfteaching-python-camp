import stats_word
text = '''
太行、王屋两座山，方圆七百里，高七八千丈。这两座山本来在冀州的南面，黄河的北面。
北山愚公，年纪将近九十岁了，面对着山居住。他苦于山北交通阻塞，进出要绕远道，就召集全家来商量说：“我要和你们尽全力挖平险峻的大山，一直通到豫州的南部，到达汉水的南岸，可以吗?”
大家纷纷地表示赞成他的意见。他的妻子提出疑问说：“凭你的力气，连像魁父那样的小山都不能削减，又能把太行、王屋(两座大山)怎么样呢?况且把挖下来的泥土石头放到哪里去呢?”大家纷纷说道：“把它们扔到渤海的边上，隐土的北面。” 
于是率领挑担子的三个儿孙，敲凿石头，挖掘泥土，用箕畚搬运到渤海的边上。邻居京城氏的寡妇有个孤儿，刚七八岁，也蹦蹦跳跳地去帮助他们。寒来暑往，季节交换，才往返一趟。
河曲智叟笑着劝阻愚公说：“你太不聪明了。凭你在世上这最后的几年，剩下的这么点力气，连山上的一棵草都铲除不了，又能把泥土石头怎么样呢?” 
北山愚公长长地叹息说：“你思想顽固，顽固到了不能通达事理的地步，连孤儿寡妇都不如。即使我死了，还有儿子在呀；儿子又生孙子，孙子又生儿子；儿子又有儿子。儿子又有孙子；子子孙孙是没有穷尽的啊。可是山却不会再增高加大，还愁什么挖不平呢?”河曲智叟没有话来回答。
山神听说愚公移山这件事，怕他不停地挖下去，就向天帝报告了这件事。天帝被愚公的诚心所感动，便命令大力神夸娥氏的两个儿子背走了两座大山，一座放在朔方的东部，一座放在雍州的南面。
从此，冀州的南部，一直到汉水的南边，再没有高山阻隔了。 
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
text_list= stats_word.stats_text(text)
print(text_list)
