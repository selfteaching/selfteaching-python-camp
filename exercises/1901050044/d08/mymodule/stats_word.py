def stats_text_en(text):
    if isinstance(text, str): #判断是否为字符串
        pass
    else:
        raise ValueError('非字符串，请重新输入。Not a string, please type again')
    punctuation = [',','.','--','*','!','?','\n',':','\'','-']
    for i in punctuation:
        text = text.replace(i," ") #将标点符号替换为空格
    text = text.lower()            #全部转换为小写
    text = text.replace('\'re', ' are') #将缩写替换为完整单词
    text = text.replace('aren\'t', ' are not')
    text = text.replace('it\'s', 'it is')
    text = text.replace('let\'s', 'let us')
    list1 = text.split(' ') #将string转换为列表，以空格分割
    for i in list1:
        if '' in list1:
            list1.remove('') #去除列表中空字符
    word_count = {}
    for word in list1:
        if not word in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    word_count = sorted(word_count.items(), key = lambda item :item[1],reverse=True)
    return word_count
 

def stats_text_cn(text):
    if isinstance(text, str):
        pass
    else:
        raise ValueError('非字符串，请重新输入。Not a string, please type again')
    punctuation = ['，','。','……','——','？','！','；','“','”',':','《','》','\n']
    for i in punctuation:
        text = text.replace(i," ")
    text1 = '' 
    for char in text: 
        text1 = text1 + char + ' ' #给每个汉字中间加上空格
    list1 = text1.split(' ') #将string转换为列表，以空格分割
    for char in list1:
        if '' in list1:
            list1.remove('') #去除列表中空字符
    char_count = {}
    for char in list1:
        if not char in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    char_count = sorted(char_count.items(), key = lambda item :item[1],reverse=True)
    return char_count

def stats_text(text):
    if isinstance(text, str):
        pass
    else:
        raise ValueError('非字符串，请重新输入。Not a string, please type again')
    en_str = '' #分别创建空中英文字符串
    cn_str = ''
    for word in text: 
        for c in word:
            if ord(c) < 128: #判断是否为英文
                en_str = en_str + word #创建包含所有英文单词的字符串
    stats_text_en(en_str)     
    for char in text:
        if u'\u4e00' <= char <= u'\u9fff': #判断是否为中文
            cn_str = cn_str + char #创建包含所有中文的字符串
    stats_text_cn(cn_str)
    return (stats_text_en(en_str)+stats_text_cn(cn_str))
