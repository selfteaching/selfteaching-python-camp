def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.!-*'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        if len(element):
            words.append(element)
    counter={}
    word_set=set(words)
    print(word_set)

    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

def  stats_text_cn(text):
    cn_characters=[]
    for character in text:
        if '\u4e00'<=character<='\u9fff':
            cn_characters.append(character)
    counter={}
    cn_characters_set=set(cn_characters)
    for character in cn_characters_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x:x[1],reverse=True)

en_text= ''' 
How The Foolish Old Man Moved Mountains

Yugong was a ninety-year-old man who lived at the north of two high mountains, Mount Taixing and Mount Wangwu.

Stretching over a wide expanse of land, the mountains blocked yugong’s way making it inconvenient for him and his family to get around.
One day yugong gathered his family together and said,”Let’s do our best to level these two mountains. We shall open a road that leads to Yuzhou. What do you think?”

All but his wife agreed with him. 
“You don’t have the strength to cut even a small mound,” muttered his wife. “How on earth do you suppose you can level Mount Taixin and Mount Wanwu? Moreover, where will all the earth and rubble go?” “Dump them into the Sea of Bohai!” said everyone.

So Yugong, his sons, and his grandsons started to break up rocks and remove the earth. They transported the earth and rubble to the Sea of Bohai.

Now Yugong’s neighbour was a widow who had an only child eight years old. Evening the young boy offered his help eagerly.

Summer went by and winter came. It took Yugong and his crew a full year to travel back and forth once.

On the bank of the Yellow River dwelled an old man much respected for his wisdom. When he saw their back-breaking labour, he ridiculed Yugong saying,”Aren’t you foolish, my friend? You are very old now, and with whatever remains of your waning strength, you won’t be able to remove even a corner of the mountain.”

Yugong uttered a sigh and said,”A biased person like you will never understand. You can’t even compare with the widow’s little boy!”

“Even if I were dead, there will still be my children, my grandchildren, my great grandchildren, my great great grandchildren. They descendants will go on forever. But these mountains will not grow any taler. We shall level them one day!” he declared with confidence.

The wise old man was totally silenced.
When the guardian gods of the mountains saw how determined Yugong and his crew were, they were struck with fear and reported the incident to the Emperor of Heavens.

Filled with admiration for Yugong, the Emperor of Heavens ordered two mighty gods to carry the mountains away.
 '''

    
cn_text='''
愚公移山

太行，王屋儿山的北面，住了一个九十岁的老翁，名叫愚公。二山占地广阔，挡住去路，是他和家人往来极为不便。

一天，愚公召集家人说：“让我们各尽其力，铲平二山，开条道路，直通豫州，你们认为怎样？”
大家都异口同声赞成，只有他的妻子表示怀疑，并说：“你连开个小土丘的力量都没有，怎可能铲平太行/王屋二山呢？况且，掘出的土石又丢到哪里去呢？”

大家都热烈的说：“把土石丢进渤海里。”
于是愚公就和儿孙，一起开挖土，把土石搬运到渤海里。
羽宫的邻居是个寡妇，有个儿子八岁也兴致勃勃地走来帮忙。
寒来暑往，他们要一年才能往返渤海一次。
住在黄河河畔的智叟，看见他们这样辛苦，取笑愚公说：“你不是很愚蠢吗？你已一把年纪了，就是用尽你的力气，也不能挖去山的一角呢？”

愚公叹息道：“你有这样的成见，是不会明白的。你比那寡妇的小儿子还不如呢！就算我死了，还有我的儿子，我的孙子，我的曾孙子，他们一直传下去。而这二山是不会加大的，总有一天，我们会把它铲平。”

智叟听了，无话可说：
二山的守护神被愚公的坚毅精神吓到，便把此事奏知天帝。天帝佩服愚公的精神，就命两位大力神背走二山。

'''


if __name__ == '__main__':
    en_result=stats_text_en(en_text)
    cn_result=stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数==>\n',en_result)
    print('统计参数中每个中文汉字出现的次数==>\n',cn_result)

def stats_text():
    stats_text_cn(cn_text)+stats_text_en(en_text)
stats_text()