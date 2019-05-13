from collections import Counter
import re
import jieba
def stats_text_en(text, count):
    """
    接收一个 text ，统计其中的英文单词出现的次数
    以下字符不计入统计：
    '!"#$%&()*+,-./:;<=>?@[]\^_`{|}~'
    """
    if  not isinstance(text, str):
        raise ValueError('输入格式错误，"text"请输入字符串（string）')

    if  not isinstance(count, int):
        raise ValueError('输入格式错误，"count"请输入整数(int)')    
 
    b = ''.join(i for i in text if i not in """!"#$%&()*+,-./:;<=>?@[\]^_`{|}~""")

    c=Counter(b.split()).most_common(count)

    return c

def stats_text_cn(text, count):
    """
    接收一个 text ，统计其中的英文单词出现的次数
    以下字符不计入统计：
    '空格、换行、0123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥…'
    """
    if  not isinstance(text, str):
        raise ValueError('输入格式错误，"text"请输入字符串（string）')
    if  not isinstance(count, int):
        raise ValueError('输入格式错误，"count"请输入整数(int)')    

    a = re.compile(r'[\u4e00-\u9fa5]')
    b=''.join(a.findall(text))
    seg_list = jieba.cut(b, cut_all=False)
    c=' '.join(seg_list)
    d=c.split()
    cnt = Counter()
    for word in d:
        if len (word) >= 2:
            cnt[word] += 1
    e= cnt.most_common(count)

    return e

    
def stats_text(text, count): 
    """
    分别调用stats_text_en和stats_text_cn方法输出合并词频统计结果
    只适用于先中文，后英文的排布，不支持中英文混排，及先英后中
    """
    if  not isinstance(text, str):
        raise ValueError('输入格式错误，"text"请输入字符串（string）')
    if  not isinstance(count, int):
        raise ValueError('输入格式错误，"count"请输入整数(int)')    
        
    import string
    #判断切分位置，根据第一个英文字母出现的位置判断
    for i in text:
        if i in string.ascii_letters:
            chai_fen_dian=text.index(i)
            #print (chai_fen_dian)
            break

    text_en=text[chai_fen_dian:]
    text_cn=text[:chai_fen_dian]
    #print(text_en)
    #print(text_cn)
    
    return stats_text_en(text_en,count) + stats_text_cn(text_cn,count)



#print(stats_text(text,count))