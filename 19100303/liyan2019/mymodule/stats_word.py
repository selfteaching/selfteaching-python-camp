# 定义一个函数，以text作为参数，统计text中英文单词频次并返回按词频降序排列的数组


def stats_text_cn(text):
    """count chinese words in text"""
    wordcount={}
    for i in text:
        if  u'\u4e00' <= i <= u'\u9fff':
            wordcount[i]=text.count(i) # [i]表示按单个字，对应英文是单个字母
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)
    return wordcount


def stats_text_en(text):
    """count english words in the text"""
    # replace useless characters
    replace_text=text.replace(',',' ').replace('.','').replace('!','').replace('*',' ').replace('-','').replace('?','')
    # split the text to words(列表)
    split_text=replace_text.split()
    wordcount={}
    for i in split_text:
        if i not in wordcount:
            # if word is not in split_text, creat a new key and let counts be 1
            wordcount[i]=1
        else:
            # if words is in split_text, let counts added 1
            wordcount[i]+=1
    # 上述if……else，与“wordcount=split_text.count(i)” 有什么区别？                
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)
    return wordcount


# 添加stats_text()函数，以调用 stats_text_cn(text) 和stats_text_en(text)，输出合并词频统计结果。

## ?? 如何调用两个函数 【原来就是两个函数相加这么简单。】
# 但是英文单词词频函数中包括了中文的情况--只要中文字中间没有空格，会将相连的中文字认定为一个单词，如何处理？】
def stats_text(text):  # 合并中英文词频统计
        """combine the stats_text_cn and stats_text_en,count english words and chinese characters"""
        a = stats_text_en(text)
        b = stats_text_cn(text)
        c = a+b
        print(c) #与前述a、b、c对齐，如果不对齐，而与 def 对齐则会出错。

text='''合并中英文词频中英文。 python useful and interesting, go and run python.'''
print(stats_text(text))
