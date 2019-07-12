import collections
def stats_text_en(text,count):
    import re
    if type(text)==str:
        text=re.sub('[^A-Za-z]',' ',txt)
        txt=txt.lower()
        txt=txt.split()
        print(collections.Counter(txt).most_common(count))
    else:
        raise ValueError('输入参数类型非字符串，请输入字符串')

def stats_text_ch(txt,count):
    import re
    if type(txt) == str:
        txt=re.sub('[^\u4e00-\u9fa5]','',txt)
        txt=txt.strip()
        print(collections.Counter(txt).most_common(count))  
    else:
        raise ValueError('输入参数类型非字符串，请输入字符串')

def stats_text(txt,count):
    stats_text_ch(txt,count)#汉字字频统计
    stats_text_en(txt,count)#英文单词词频统计