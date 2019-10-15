#将英文进行词频统计。
def stats_text_en(text):
    if type(text) == str:
        #去除字符串中的中文字符
        for chara in text:
            if '\u4e00' <= chara <= '\u9fa5':
                text = text.replace(chara,",")
        #清洗英文字符串中的特殊字符
        for chara in ",.!-*？，。：「」、”":
            text = text.replace(chara," ")
        #将字符串中的英文全部变成小写
        text = text.lower()
        list1 = text.split()
        counts = {}
        #统计每个单词出现的词频
        for word in list1:
            counts[word] = counts.get(word,0) + 1
        list2 = list(counts.items())
        #将单词词频进行降序排序
        list2.sort(key=lambda x:x[1], reverse=True)
        return print(list2)
    else:
        raise ValueError("The input is a non-string, please enter a string.")

#将中文进行词频统计。
def stats_text_cn(text):
    if type(text) == str:
        list1 = []
        counts = {}
        #选取字符串中的中文字符
        for chara in text:
            if '\u4e00' <= chara <= '\u9fa5':
                list1.append(chara)
        #统计字符串中的中文词频
        for i in list1:
            counts[i] = counts.get(i,0) + 1
        list2 = list(counts.items())
        #将统计后的中文词频按降序排序
        list2.sort(key=lambda x: x[1], reverse=True)
        return print(list2)
    else:
        raise ValueError("The input is a non-string, please enter a string.")

#分别调用stats_text_en()函数和stats_text_cn()函数。
def stats_text(text):
    if type(text) == str:
        stats_text_en(text)
        stats_text_cn(text)
    else:
        raise ValueError("The input is a non-string, please enter a string.")