from mymodule import stats_word
text='''
定投

投资，是我能找到的唯一一个普通人可以跨越阶层的通路。而定投则是唯一一种所有普通人都有机会做、并且都有能力做好的投资方式。

所谓的定投，就是针对某个投资标的在很长的时间内定期投资一定的金额。

例如，在未来的 5 到 10 年之中（很长的时间），每周（定期）投资 BOX 这个无管理费的区块链 ETF 产品（投资标的）150 美元或者 1000 元人民币（一定的金额）…… 当然，你可以把 BOX 替换为任何值得长期投资并持有的标的，比如苹果公司股票、贵州茅台股票，可口可乐股票，或者标准普尔指数基金。

在任何一个社会，在任何一个时代，绝大多数人都处于终生抱怨的状态。然而，在今天这个时代 —— 今天这个有着自由且成熟的证券交易市场存在的时代 —— 绝大多数终生抱怨的人其实并不知道他们每个人（对，就是每个人）都实际上因为无知错过了自己摆脱一切抱怨的机会。

可自由参与的证券交易市场，是当今现代世界里的奇迹 —— 正是因为它的存在，所有的普通人才有了至高无上的机会 —— 这一点书中会详细论述。
How The Foolish Old Man Moved Mountains
Yugong was a ninety-year-old man who lived at the north of two high
mountains, Mount Taixing and Mount Wangwu.
Stretching over a wide expanse of land, the mountains blocked
yugong’s way making it inconvenient for him and his family to get
around.
One day yugong gathered his family together and said,”Let’s do our
best to level these two mountains. We shall open a road that leads
to Yuzhou. What do you think?”
All but his wife agreed with him.
“You don’t have the strength to cut even a small mound,” muttered
his wife. “How on earth do you suppose you can level Mount Taixin
and Mount Wanwu? Moreover, where will all the earth and rubble go?”
“Dump them into the Sea of Bohai!” said everyone.
So Yugong, his sons, and his grandsons started to break up rocks and
remove the earth. They transported the earth and rubble to the Sea
of Bohai.

Now Yugong’s neighbour was a widow who had an only child eight years
old. Evening the young boy offered his help eagerly.

Summer went by and winter came. It took Yugong and his crew a full
    year to travel back and forth once.

On the bank of the Yellow River dwelled an old man much respected
    for his wisdom. When he saw their back-breaking labour, he ridiculed
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
  When the guardian gods of the mountains saw how determined Yugong
    and his crew were, they were struck with fear and reported the
    incident to the Emperor of Heavens.

  Filled with admiration for Yugong, the Emperor of Heavens ordered
    two mighty gods to carry the mountains away.

'''
result = stats_word.stats_text(text)

print('统计结果:',result)