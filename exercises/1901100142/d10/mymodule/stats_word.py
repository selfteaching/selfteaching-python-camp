from collections import Counter
import jieba

text = ''' 
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

def stats_text_cn(text,num):
    if type(text) != str:
        raise ValueError('you should give a string!')
    words_ch = jieba.cut(text)
    words_list = []
    for word in words_ch:
        if len(word) > 1:
            words_list.append(word)
    return Counter(words_list).most_common(num)


if __name__ == '__main__':
    result_all = stats_text_cn(text,15)
    print(result_all)