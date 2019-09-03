# this script is to write a function to call other functions

# 1 for english word
def stats_text_en(text):
    text = text.strip().split()
    words = [] # for store the text after processing
    symbols = '、??:「」，。.!,“”'
    for word in text:
        for  symbol in symbols:
            word = word.replace(symbol,'') # delet the redundant symbols in the text
        words.append(word)

    word_set = set(words) # transfer the list to the set
    counter_dict = {}

    for word in word_set: # count the number for each word
        counter_dict[word] = words.count(word)

    Result = sorted(counter_dict.items(),key = lambda x: x[1], reverse = True)
    
    return Result


# 2 for chinese word
def stats_text_cn(text):
    # text = text.strip().split() # this is not required, since han char is a char,we can process it directly 
    characters_cn = [] # for storing the text after processing

    for character in text:
        if '\u4e00'<= character <= '\u9fff':
            characters_cn.append(character)
    characters_set = set(characters_cn) # transfer the list to the set

    counter_dict = {}

    for character in characters_set: # count the number for each word
        counter_dict[character] = characters_cn.count(character) # for a dict{key,value} this is: dict[key] = value (value is the frequencies for the word)
    Result = sorted(counter_dict.items(),key = lambda x: x[1], reverse = True)

    return Result

# 3 the function which calls the above 2 functions
def stats_text(text):

    # for chinese words
    Result_cn = stats_text_cn(text)

    # for english words
    # remove of the chinese characters in the text
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            text = text.replace(character,'')
    # print("seeeeeeee no chinese okay",text)
    Result_en = stats_text_en(text) # text is non-chinese text

    Result = Result_cn + Result_en # list + list

    return Result



text = '''
愚公移 
太 ，王屋  的  ，住  個九 歲的 翁，名叫愚公。  佔地廣闊，擋住去 ，使他
和家 往 極為  。
 天，愚公召集家 說:「讓我們各盡其 ，剷平  ，開條道 ，直通豫州，你們認為怎
樣?」
 家都  同聲贊成，只有他的妻 表示懷疑，並說:「你連開鑿 個 丘的  都沒有，怎
可能剷平太 、王屋  呢?況且，鑿出的   丟到哪裏去呢?」
 家都熱 地說:「把  丟進渤 裏。」
於是愚公就和兒孫， 起開挖 ，把  搬運到渤 去。
愚公的鄰居是個寡婦，有個兒  歲也興致勃勃地  幫忙。
寒 暑往，他們要  才能往返渤  次。
住在 河河畔的智叟，看 他們這樣 苦，取笑愚公說:「你 是很愚蠢嗎?你已 把 紀
 ，就是 盡你的氣 ，也 能挖去 的  呢?」
愚公歎息道:「你有這樣的成 ，是 會明 的。你 那寡婦的 兒 還 如呢!就算我死
 ，還有我的兒 ，我的孫 ，我的曾孫 ，他們 直傳下去。 這  是 會加 的，總有
 天，我們會把它們剷平。」
智叟聽 ，無話可說:
  的守護神被愚公的堅毅精神嚇倒， 把此事奏知天帝。天帝佩服愚公的精神，就命兩位 
 神揹   。
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

Yugong uttered a sigh and said,” A biased person like you will never
understand. You can’t even compare with the widow’s little boy!”

“Even if I were dead, there will still be my children, my
grandchildren, my great grandchildren, my great great grandchildren.
They descendants will go on forever. But these mountains will not
grow any taler. We shall level them one day!” he declared with
confidence.

The wise old man was totally silenced.
4When the guardian gods of the mountains saw how determined Yugong
and his crew were, they were struck with fear and reported the
incident to the Emperor of Heavens.

Filled with admiration for Yugong, the Emperor of Heavens ordered
two mighty gods to carry the mountains away.
'''


if __name__ == "__main__":
    # a example calling the function english text
    # print('the sorted word frequencies for the input english text \n',stats_text_en(text_sample))
    # # a example calling the function chinese text
    # print('the sorted word frequencies for the input chinese text \n',stats_text_cn(text_sample1))
    print("The result combining statistic of Chinese words and English words \n",stats_text(text))

