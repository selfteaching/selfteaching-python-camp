 # 统计text中每个英语单词出现的次数
def stats_text_en(text):
    if not isinstance(text, str):
        raise ValueError('参数必须是str类型,输入类型%s'%type(text))
    words = []
    elements = text.split()
    for e in elements:
        for s in ',.*-!':
            e = e.replace(s,'') # 把每个单词里的特殊符号清除掉
        if len(e) and e.isascii():# 过滤掉中文
            words.append(e)
    counter ={}
    wordset = set(words)
    for w in wordset:
        counter[w] = words.count(w)
    
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)

# 统计text中每个汉字出现的次数。返回一个字频降序排序的数组
def stats_text_cn(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s'%type(text))
    cn_characters = []
    for character in text:
        if '\u4e00' <= character <= '\u9fff' : # 是中文
            cn_characters.append(character)
   
    counter = {}
    wordset = set(cn_characters)
    for w in wordset:
        counter[w] = text.count(w)
    return sorted(counter.items(),key=lambda x: x[1],reverse=True)


def stats_tex(text):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s' % type(text))
    en = stats_text_en(text)
    cn = stats_text_cn(text)
    return en+cn


    