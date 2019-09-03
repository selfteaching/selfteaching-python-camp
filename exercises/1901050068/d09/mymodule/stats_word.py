# 1. 统计中文汉字字频
# 2. 统计英文单词词频

from collections import Counter  # 提供了可哈希对象的计数功能

# 统计中文汉字字频的函数
def stats_text_cn(text_cn,count): 

    if not isinstance(text_cn,str):  # 判断text_cn是否为字符串类型
        raise ValueError(f'输入的参数是{type(text_cn)}类型，不是字符串类型。')       

    cnt = Counter()      
     
    for word in text_cn: 
        if '\u4e00' <= word <= '\u9fff':   # 中文字符范围，清洗字符串，只保留汉字
            cnt[word] += 1   # 统计汉字词频        
            
    return Counter(cnt).most_common(count)  # # 输出词频最高的前100个汉语词语
   

# 统计英文单词词频的函数
def stats_text_en(text_en,count):  

    if not isinstance(text_en,str):  # 判断text_en是否为字符串类型
        raise ValueError(f'输入的参数是{type(text_en)}类型，不是字符串类型。') 
     
    t = text_en.replace(',',' ').replace('.',' ').replace('-',' ').replace('"',' ').replace('!',' ').replace('?',' ') 
    # 将非英文字符替换为空格

    cnt = Counter()
    my_list = ''    # 存储英文单词的字符串

    for s in t:  # 只保留英文单词
        if s.isascii():
            my_list += s

    t = my_list.lower()   # 把大写转换为小写        
    t = t.split()   # 以空格，把字符串内单词拆分为列表

    for word in t:  
        cnt[word] += 1  # 统计英文单词词频

    return Counter(cnt).most_common(count)  # 输出词频最高的前100个英语单词


def stats_text(text,count):

    if not isinstance(text,str):   # 判断text是否为字符串类型
        raise ValueError(f'输入的参数是{type(text)}类型，不是字符串类型。')   

    print(stats_text_cn(text,count))  # 输出中文汉字字频

    print(stats_text_en(text,count))  # 输出英语单词词频


