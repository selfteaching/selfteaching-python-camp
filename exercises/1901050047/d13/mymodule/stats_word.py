from collections import Counter  # 提供了可哈希对象的计数功能
import jieba   # 结巴中文分词
import re   # 正则表达式

# 统计中文词频的函数
def stats_text_cn(text_cn,count): 

    if not isinstance(text_cn,str):  # 判断text_cn是否为字符串类型
        raise ValueError(f'输入的参数是{type(text_cn)}类型，不是字符串类型。')   

    p = re.compile('[^\u4e00-\u9fa5]')  # 只保留中文字符，不包含标点符号
    zh = "".join(p.split(text_cn)).strip()  # 把文字链接在一起，没有空格（保留空格也可以，分词的结果一样）
    
    # seg_list = jieba.cut(zh, cut_all=True)   # 全模式，把句子中所有的可以成词的词语都扫描出来
    seg_list = jieba.cut_for_search(zh)   # 适合用于搜索引擎构建倒排索引的分词，粒度比较细

    cnt = []
    for word in seg_list:
        if len(word) >= 2:  # 统计长度大于等于2的词 
            cnt.append(word)
                     
    return Counter(cnt).most_common(count)  # 输出词频最高的前100个单词
 

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

    print(type(Counter(cnt).most_common(count)))
    return Counter(cnt).most_common(count)  # 输出英文单词词频


def stats_text(text,count):

    if not isinstance(text,str):   # 判断text是否为字符串类型
        raise ValueError(f'输入的参数是{type(text)}类型，不是字符串类型。')   

    print(stats_text_cn(text,count))  # 输出中文汉字字频

    print(stats_text_en(text,count))  # 输出英文单词词频