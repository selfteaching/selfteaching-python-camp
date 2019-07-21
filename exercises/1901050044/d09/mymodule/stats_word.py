import collections
import re
top_n = int()
def stats_text_en(text, top_n = None):
    if isinstance(text, str): #判断是否为字符串
        pass
    else:
        raise ValueError('非字符串，请重新输入。Not a string, please type again')
    punctuation = [',','.','--','*','!','?','\n',':','-']
    for i in punctuation:
        text = text.replace(i," ") #将标点符号替换为空格
    text = text.replace('\'re', ' are') #将缩写替换为完整单词
    text = text.replace('aren\'t', ' are not')
    text = text.replace('it\'s', 'it is')
    text = text.replace('let\'s', 'let us')
    text = text.replace('can\'t', 'can not')
    text = text.replace('I\'m', 'I am')
    words = re.findall(r'\w+',text.lower())
    return collections.Counter(words).most_common(top_n)
 

def stats_text_cn(text, top_n = None):
    if isinstance(text, str):
        pass
    else:
        raise ValueError('非字符串，请重新输入。Not a string, please type again')
    punctuation = ['，','。','……','——','？','！','；','“','”',':','《','》','\n']
    for i in punctuation:
        text = text.replace(i," ") #将标点符号替换为空格
    text1 = ''
    for char in text:
        text1 = text1 + char + ' '
    chars = re.findall(r'[\u4e00-\u9fa5]+', text1)
    return collections.Counter(chars).most_common(top_n)
    
def stats_text(text,top_n = None):
    if isinstance(text, str):
        pass
    else:
        raise TypeError
    en_str = '' #分别创建空中英文字符串
    cn_str = ''
    for word in text: 
        for c in word:
            if ord(c) < 128: #判断是否为英文
                en_str = en_str + word #创建包含所有英文单词的字符串
    stats_text_en(en_str)     
    for char in text:
        if u'\u4e00' <= char <= u'\u9fff': #判断是否为中文
            cn_str = cn_str + char  #创建包含所有中文的字符串
    stats_text_cn(cn_str)
    return (stats_text_en(en_str, top_n), stats_text_cn(cn_str, top_n))

