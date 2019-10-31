from collections import Counter
import array
import jieba

#统计参数中每个英文单词出现的次数
def stats_text_en(text, count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol,'')
        #用 str 类型 的 isascii 方法判断是否为英文单词
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)



    '''for word in word_set:
        counter[word] = words.count(word)
    #函数返回值用 return 进行返回，如过没有 return 返回值则为 None
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)'''


#统计参数中每个中文汉字出现的次数
def stats_text_cn(text, count):
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)




#seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
#print("Default Mode: " + "/ ".join(seg_list))  # 精确模式


def stats_text(text, count):

    
    #合并 英文词频 和 中文词频 的结果
    
    return stats_text_en(text, count) + stats_text_cn(text, count)


#搜索 __name__ == '__main__'
#一般情况下在文件内 测试 代码的时候以下面的形式进行
