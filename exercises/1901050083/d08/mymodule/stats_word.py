def stats_text_en(text):
    """
    接收一个 text ，统计其中的英文单词出现的次数
    以下字符不计入统计：
    '!"#$%&()*+,-./:;<=>?@[]\^_`{|}~'
    """

    if  not isinstance(text, str):
        raise ValueError('输入格式错误，请输入字符串（string）')
    a = {}

    b = ''.join(i for i in text if i not in """!"#$%&()*+,-./:;<=>?@[\]^_`{|}~""")

    for word in b.split():
        if word not in a:
            a[word] = 1
        else:
            a[word] += 1
   
    c = sorted(a.items(),key=lambda x:x[1],reverse=True)
    return c

def stats_text_cn(text):
    """
    接收一个 text ，统计其中的英文单词出现的次数
    以下字符不计入统计：
    '空格、换行、0123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥…'
    """
    if  not isinstance(text, str):
        raise ValueError('输入格式错误，请输入字符串（string）')

    a = {}
    
    b = ''.join(i for i in text if i not in """\n\u30000123456789!"#$%&()*+,-./:;<=>?@[\]^_`{|}~，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥…""")

    for word in b:
        if word not in a:
            a[word] = 1
        else:
            a[word] += 1
   
    c = sorted(a.items(),key=lambda x:x[1],reverse=True)
    return c
    
def stats_text(text): 
    """
    分别调用stats_text_en和stats_text_cn方法输出合并词频统计结果
    只适用于先中文，后英文的排布，不支持中英文混排，及先英后中
    """
    if  not isinstance(text, str):
        raise ValueError('输入格式错误，请输入字符串（string）')
        
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
    
    print(stats_text_en(text_en) + stats_text_cn(text_cn))

    
text="""拉萨的肌肤顺利打开房间aslkdjf  sldkfj  sdlfkj asld f
"""
