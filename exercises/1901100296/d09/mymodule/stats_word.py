import collections

# 封装统计英文单词词频的函数
def stats_text_en(text,count) :
    if type(text)==str:
        list_text=text.lower().split()
        words=[]
        #剔除特殊字符并删除空字符
        symbols='*--?!.,:，、。「」'
        for word in list_text:
                for symbol in symbols:
                    word=word.replace(symbol,'')
                # if len(word)and word<'\u4e00' or word>'\u9fff':
                # if word.encode('UTF-8').isalpha():
                if len(word) and word.isascii():
                        words.append(word)
        # 使用字典类型统计文本中单词数
        # word_dic={}
        # keys_set=set(words)
        # for word in keys_set:
        #     word_dic[word]=words.count(word)  
        # # 对字典的值降序排列
        # return sorted (word_dic.items(),key=lambda item:item[1],reverse=True)
        cnt=collections.Counter()
        for word in words:
            cnt[word] += 1
        return collections.Counter(words).most_common(count)
    # ex=ValueError('参数值错误！')
    # raise ex
# 封装统计汉字词频的函数
def stats_text_cn(text,count):
    if type(text)==str:
        # 挑拣汉字出来
        words=[]
        for word in text:
            if '\u4e00' <= word <= '\u9fff':
                words.append(word)
        # 统计文本中汉字个数
        # word_dic={}
        # keys_set=set(words)
        # for word in keys_set:
        #     word_dic[word]=words.count(word)
        # # 对字典值降序排列
        # return sorted (word_dic.items(),key=lambda item:item[1],reverse=True)
        # 使用标准库的Counter统计词频，并排序输出
        cnt=collections.Counter()
        for word in words:
            cnt[word] += 1
        return collections.Counter(words).most_common(count)
    ex=ValueError('参数值错误！')
    raise ex
# 统计英文和汉字的函数
def stats_text(text,count):
        return(stats_text_cn(text,count)+stats_text_en(text,count))
