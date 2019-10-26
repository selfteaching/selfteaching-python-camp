#任务1：封装统计英文单词词频的函数
def stats_text_en(text): 
    text2 = text.lower().split()
    words = []
    for i in range(len(text2)):
        text2[i]=text2[i].strip(',.--*!\'')
        if len(text2[i]):
            words.append(text2[i]) #只统计英文单词
    word_dic = {}
    for key in words:
        if key in word_dic:
            word_dic[key] += 1
        else:
            word_dic[key] = 1 #统计各英文单词出现的次数
    word_sorted = sorted(word_dic.items(), key = lambda x : x[1], reverse = True)
    #按照出现次数从大到小输出所有的单词及出现的次数
    return dict(word_sorted)



#任务2：封装统计中文汉字字频的函数
def stats_text_cn(text):
    text2 = list(text)
    words = []
    for i in text2:
        if '\u4e00' <= i <= '\u9fff': #中文字符范围
            words.append(i)
    word_dic = {}
    for key in words:
        if key in word_dic:
            word_dic[key] += 1
        else:
            word_dic[key] = 1 #统计各中文单词出现的次数
    word_sorted = sorted(word_dic.items(), key = lambda x : x[1], reverse = True)
    #按照出现次数从大到小输出所有的单词及出现的次数
    return dict(word_sorted)