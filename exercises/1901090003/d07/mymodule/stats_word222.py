import re
# 封装统计英文单词词频的函数
def stats_text_en(text):
    # 1.替换掉所有的符号
    word_str = re.findall(r'\b[a-z]+\'?[a-z]+',text.lower())
    # 2.按照空格将所有的单词分割开
    word_list = word_str.split( )
    # 3.对单词进行去重操作，作为字典的key
    word_one = set(word_list)
    # 4.构建一个词频字典
    dict = {}
    for word in word_one:
        dict[word] = word_list.count(word)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list

# 封装统计中文汉字字频的函数
def stats_text_cn(text):
    # 如果不是字符串，给出提示
    if not isinstance(text,str):
        return '请输入字符串'

    # 1.首先将乱七八糟的符号去掉，方便之后的匹配
    # 2.将上面字符串中的英文以及数字替换为空，即删除
    d = re.sub(r'[\Wa-zA-Z0-9]','',text)
    print(d)
    # 3.将字符串中的汉字去重，作为字典的key
    d_list = list(d)
    print(d_list)
    d_index = set(d_list)
    # 4.构造词频字典
    dict = {}
    for i in d_index:
        dict[i] = d_list.count(i)
    # 5.对之前的词频字典按照value值进行排序
    d_list = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    return d_list


def stats_text(text):
    arr_en = stats_text_en(text)
    arr_cn = stats_text_cn(text)
    arr_all = sorted((arr_en + arr_cn),key = lambda x:x[1],reverse = True)
    return arr_all
# 调用上述两个函数    
   

