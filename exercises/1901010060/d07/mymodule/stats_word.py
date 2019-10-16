def stats_text_en(text): #统计英文单词出现的次数，按词频降序排列
    text=text.lower()   #把单词全部变为小写
    for p1 in ['~','!','@','#','$','%','^','&','*','(',')','_','+','|','{','{','[','.','-',',',';',':']:
        text=text.replace(p1," ")  #去除标点符号
    text=text.split()   #把字符串分割成单个单词列表
    d1={}
    for s in text:
        if (s >= u'\u0041' and s<=u'\u005a') or (s >= u'\u0061' and s<=u'\u007a'):
            d1.setdefault(s,text.count(s))
    d1 = sorted(d1.items(), key=lambda y: y[1], reverse=True) 
    return d1


def stats_text_cn(text):    #统计中文汉字出现的次数，按词频降序排列
    for p2 in ['！','@','￥','%','……','&','*','（','）','—','+','{','}','：','“','《','》','？','，','。','、','；']:
        text=text.replace(p2," ")  #去除标点符号
    d2={}
    for s in text:
        if '\u4e00' <= s <= '\u9fff':   # 中文字符范围
            d2.setdefault(s,text.count(s))
    d2 = sorted(d2.items(), key=lambda y: y[1], reverse=True) 
    return d2


def stats_text(text):   #统计英文单词词频和中文汉字字频出现的次数，按词频降序排列
     print(en_result)

     print(cn_result)


#测试
print(stats_text_cn(text)+stats_text_en(text))