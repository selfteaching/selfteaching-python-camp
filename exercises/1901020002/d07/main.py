from mymodule import stats_word

sample_text = ''' 
愚公移山

太行, 王屋两座山, 方圆七百里, 高七八千丈, 本来在冀州南边, 黄河北岸的北边。
北山下面有个名叫愚公的人,在山的正对面居住。
他苦于山区北部的阻塞，出来进去都要绕道，就召集全家人商量说，我跟你们尽力挖平险峻的大山，使道路一直通到豫州南部，到达汉水南岸，好吗

How The Foolish Old Man Moved Mountains

Yugong was a ninety-year-old man who lived at the north of two high mountains, Mount Taixing and Mount Wangwu.

Stretching over a wide expanse of land, the mountains blocked yugong's way making it inconvenient for him and his family to get around. 
One day yugong gathered his family together and said," Let’s do our best to level these two mountains. We shall open a road that leads to Yuzhou. What do you think?"

All but his wife agreed with him. "You don’t have the strength to cut even a small mound," muttered his wife. "How on earth do you suppose you can level Mount Taixin and Mount Wanwu? Moreover, where will all the earth and rubble go?" "Dump them into the Sea of Bohai!" said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and remove the earth. They transported the earth and rubble to the Sea of Bohai.
Now Yugong’s neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.
Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.
On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed Yugong saying," Aren’t you foolish, my friend? You are very old now, and with whatever remains of your waning strength, you won’t be able to remove even a corner of the mountain."
Yugong uttered a sigh and said,"A biased person like you will never understand. You can’t even compare with the widow’s little boy!"
"Even if I were dead, there will still be my children, my grandchildren, my great grandchildren, my great great grandchildren. They descendants will go on forever. But these mountains will not grow any taler. We shall level them one day!" he declared with confidence.
The wise old man was totally silenced. When the guardian gods of the mountains saw how determined Yugong and his crew were, they were struck with fear and reported the incident to the Emperor of Heavens.
Filled with admiration for Yugong, the Emperor of Heavens ordered two mighty gods to carry the mountains away.
'''
result = stats_word.stats_text(sample_text)
print('输出统计结果', result)