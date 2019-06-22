# this script is to write a function which implements the dictionary in which doing number counting of the words, 
# sort the words in the dict 

# 1 for english word
def stats_text_en(text,symbols):
    text = text.strip().split()
    words = [] # for store the text after processing
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
def stats_text_cn(text,symbols):
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


# Examples for the above two functions
text_sample = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
symbols = '.,*-!'

text_sample1 = '''
《红楼梦》的主题本身并不复杂，其复杂方面主要反映在内涵上。
小说中对人物的研究、对人与人之间各种情感的描写也都非常高深，
几乎是一部感情科学专著。小说写的是一个极其富有、倍受皇帝赏识的大家族，
而事实上这个家族原来的一个成员（入宫）成了皇妃。但小说正是从这个家庭的家财散尽、
昔日风光不再、开始走向没落入手的。这个家庭的最后一个、也是唯一的儿子贾宝玉，
因为受到家庭内部腐败的影响，也日渐堕落。他出生时，嘴里含着一块具有象征意义的玉石，
而让他拥有特殊的地位。小说的引子写道：很久以前，天破了一个大口，（女娲）修补（缺口）时，
剩下一小块（石头），于是成了贾宝玉的那块名玉。
中国人对超自然力一直就有兴趣，而时至今日，这种信仰还是中国人生活的一部分。
This novel seized hold of the people primarily because it portrayed the problems of their own family system, 
the absolute power of women in the home, the too great power of the matriarchy,
the grandmother, the mother, and even the bondmaids, so often young and beautiful 
and fatally dependent, who became too frequently the playthings of the sons of the 
house and ruined them and were ruined by them. Women reigned supreme in the Chinese house, 
and because they were wholly confined in its walls and often illiterate, they ruled to the hurt of all. 
They kept men children, and protected them from hardship and effort when they should not have been so protected.
Such a one was Chia Pao Yü, and we follow him to his tragic end in Hung Lou Meng. 
'''
symbols1 = '.,*-!。，/、？《》（）'

if __name__ == "__main__":
    # a example calling the function english text
    print('the sorted word frequencies for the input english text \n',stats_text_en(text_sample,symbols))
    # a example calling the function chinese text
    print('the sorted word frequencies for the input chinese text \n',stats_text_cn(text_sample1,symbols1))

