import string


def stats_text_en(en_text):
    # clean data by removing the special words
    for en_special_word in string.punctuation:
        if en_special_word in en_text:
            en_text = en_text.replace(en_special_word, "")

    # generate a dict to calculate the frequency of each word
    en_word_count = {}
    en_text = en_text.split()
    for en_word in en_text:
        en_word_count.setdefault(en_word, 0)
        en_word_count[en_word] += 1

    # sort the dict
    en_sorted_words = sorted(en_word_count.items(), key=lambda obj: obj[1], reverse=True)

    # return the word and frequency list
    return en_sorted_words
    # only return the word list
    # return [word for word, freq in en_sorted_words]


def stats_text_cn(cn_text):
    # define the special word in CN
    cn_special_words = "！“”#$%&‘’（）*+，-。/：；、……<=>？@[]《》^_`{|}~\n"
    for cn_special_word in cn_special_words:
        if cn_special_word in cn_text:
            cn_text = cn_text.replace(cn_special_word, "")

    cn_word_count = {}
    for cn_word in cn_text:
        cn_word_count.setdefault(cn_word, 0)
        cn_word_count[cn_word] += 1

    cn_sorted_words = sorted(cn_word_count.items(), key=lambda obj: obj[1], reverse=True)

    return cn_sorted_words
    # return [word for word, freq in cn_sorted_words]

if __name__ == "__main__":
    en_string = '''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
    it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
    print(stats_text_en(en_string))

    cn_string = '''最高人民法院审理认为，滨河集团使用的标识是“滨河九粮液”“滨河九粮春”、
“九粮液”、“九粮春”，其中“滨河九粮液”、“滨河九粮春”的“滨河”二字较小，“九粮液”“九粮春”三字较为突出。
被诉侵权标识“九粮液”“九粮春”与“五粮液”、“五粮春”相比，仅一字之差，且区别为两个表示数字的文字，
考虑到“五粮液”、“五粮春”系列商标的知名度，使用“九粮液”“九粮春”易使相关公众对商品的来源产生混淆误认。'''
    print(stats_text_cn(cn_string))