#统计参数中每个英文单词出现的次数
import string


def stats_text_en(words):



    #初始化一个counter字典，用来存放单词出现的频次
    counter = {}

    #去重，减少迭代次数
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)

    #2.从小到大排序输出

    return sorted(counter.items(), key = lambda x:x[1],reverse=True)

#统计参数中每个中文字符出现的次数
def stats_text_cn(words):
    str_words = ''.join(words)
    set_words = set(str_words)

    counter = {}

    for ch in set_words:
        counter[ch] = str_words.count(ch)
    return sorted(counter.items(),key = lambda x:x[1],reverse=True)

def stats_text(text):

    symbols = '，。:「」,?.”、-!'
    for symbol in symbols:
        text = text.replace(symbol,' ')
    l1 = text.split()
    en_text = []
    cn_text = []
    for i in l1:
        if len(i)>0:
            if i[0] in string.ascii_letters:
                en_text.append(i)
            else:
                cn_text.append(i)
        
    cn_result = stats_text_cn(cn_text)
    en_result = stats_text_en(en_text)
    merged_result = cn_result+en_result
    return (merged_result)
















    
