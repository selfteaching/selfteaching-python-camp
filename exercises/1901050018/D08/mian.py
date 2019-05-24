text = '''
愚公移山
太行、王屋两座山，方圆七百里，高七八千丈，本来在冀州南边，黄河北岸的北边。
北山下面有个名叫愚公的人，年纪快到90岁了，在山的正对面居住。他苦于山区北部的阻塞，出
来进去都要绕道，就召集全家人商量说：“我跟你们尽力挖平险峻的大山，（使道路）一直通到豫州南
部，到达汉水南岸，好吗？”大家纷纷表示赞同。他的妻子提出疑问说：“凭你的力气，连魁父这座小山
都不能削平，能把太行、王屋怎么样呢？再说，往哪儿搁挖下来的土和石头？”众人说：“把它扔到渤海
的边上，隐土的北边。”于是愚公率领儿孙中能挑担子的三个人（上了山），凿石头，挖土，用箕畚运
到渤海边上。邻居京城氏的寡妇有个孤儿，刚七八岁，蹦蹦跳跳地去帮助他。冬夏换季，才能往返一次。
河湾上的智叟讥笑愚公，阻止他干这件事，说：“你简直太愚蠢了！就凭你残余的岁月、剩下的力
气连山上的一棵草都动不了，又能把泥土石头怎么样呢？”北山愚公长叹说：“你的心真顽固，顽固得没
法开窍，连孤儿寡妇都比不上。即使我死了，还有儿子在呀；儿子又生孙子，孙子又生儿子；儿子又
有儿子，儿子又有孙子；子子孙孙无穷无尽，可是山却不会增高加大，还怕挖不平吗？”河曲智叟无话可答。
握着蛇的山神听说了这件事，怕他没完没了地挖下去，向天帝报告了。天帝被愚公的诚心感动，
命令大力神夸娥氏的两个儿子背走了那两座山，一座放在朔方的东部，一座放在雍州的南部。从这时
开始，冀州的南部直到汉水南岸，再也没有高山阻隔了。
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
try:
    stats_word.stats_text(text)
except ValueError:
    print('请输入非字符串')
print(stats_word.stats_text(text))