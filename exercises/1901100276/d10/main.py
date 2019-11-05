from mymodule import stats_word
text = '''
愚 公 移 ⼭
太 ⾏，王 屋 ⼆ ⼭ 的 北 ⾯ ， 住 了 ⼀ 個 九 ⼗ 歲 的 ⽼ 翁 ， 名 叫 愚 公 。 ⼆ ⼭ 佔 地 廣 闊 ， 擋 住 去 路 ， 使 他 
和 家 ⼈ 往 來 極 為 不 便 。
⼀ 天 ， 愚 公 召 集 家 ⼈ 說 ： 「 讓 我 們 各 盡 其 ⼒ ， 剷 平 ⼆ ⼭ ， 開 條 道  路 ， 直 通 豫 州 ， 你 們 認 為 怎
樣 ？」
⼤ 家 都 異 ⼝ 同 聲 贊  成 ， 只 有 他 的 妻 ⼦ 表 示 懷 疑 ， 並 說 ： 「 你 連 開 鑿 ⼀ 個 ⼩ 丘 的 ⼒ 量 都 沒 有 ，怎
可 能 剷 平 太 ⾏ 、 王 屋 ⼆ ⼭ 呢 ？ 況 且 ， 鑿 出 的 ⼟ ⽯ ⼜ 丟 到 哪 裏 去 呢 ？」
⼤ 家 都 熱 烈 地 說 ： 「 把 ⼟ ⽯ 丟 進 渤 海 裏 。」
於 是 愚 公 就 和 兒 孫 ， ⼀ 起 開 挖 ⼟ ， 把 ⼟ ⽯ 搬 運 到 渤 海 去。
愚 公 的 鄰 居 是 個 寡 婦 ， 有 個 兒 ⼦ ⼋ 歲 也 興 致 勃 勃 地⾛ 來 幫 忙。
寒 來 暑 往 ， 他 們 要 ⼀ 年 才 能 往 返 渤 海 ⼀ 次 。
住 在 ⿈ 河 河 畔 的 智 叟 ， 看 ⾒ 他 們 這 樣 ⾟ 苦 ， 取 笑 愚 公 說 ：「你 不 是 很 愚 蠢 嗎 ？ 你 已 ⼀ 把 年 紀 
了 ， 就 是 ⽤ 盡 你 的 氣 ⼒ ， 也 不 能 挖 去 ⼭ 的 ⼀ ⻆ 呢 ？ 」
愚 公 歎 息 道 ： 「 你 有 這 樣 的 成 ⾒ ， 是 不 會 明 ⽩ 的 。 你 ⽐ 那 寡 婦 的 ⼩ 兒 ⼦ 還 不 如 呢 ！ 就 算 我 死 
了 ， 還 有 我 的 兒 ⼦ ， 我 的 孫 ⼦ ， 我 的 曾 孫 ⼦ ，他 們 ⼀ 直 傳 下 去 。 ⽽ 這 ⼆ ⼭ 是 不 會 加 ⼤ 的 ， 總 有 
⼀ 天 ， 我 們 會 把 它 們 剷 平 。 」
智 叟 聽 了 ， 無 話 可 說 ：
⼆ ⼭ 的 守 護 神 被 愚 公 的 堅 毅 精 神 嚇 倒 ， 便 把 此 事 奏 知 天 帝。天 帝 佩 服 愚 公 的 精 神 ， 就 命 兩 位 ⼤ 
⼒ 神 揹 ⾛ ⼆ ⼭ 。
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
with open(r'C:\Users\Administrator.PC-201904091527\Documents\GitHub\selfteaching-python-camp\exercises\1901100276\d09\mymodule\tang300.json','r',encoding='UTF-8')as f:
    b= f.read()
#a= stats_word.stats_text(text)
#print(a)
def main():
    try:
        print (stats_word.stats_text(b,20))
    except ValueError as e:
        print('报错:{0}\n',format(e))
main()