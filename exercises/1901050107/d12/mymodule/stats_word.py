
import jieba
# 分别调⽤用stats_text_en , stats_text_cn ，输出合并词频统计结果
# 统计参数中每个英⽂文单词出现的次数，最后返回⼀个按词频降序排列列的数组
from functools import reduce
from collections import Counter

def stats_text_en(text,count):
    if not isinstance(text,str):
        raise ValueError("text is not a string")
    # 将单词分离出来
    result = text.split()
    word_list = []
    symple_set = ",.-!?"
    cnt = Counter()
    for item in result:
        # 排除单词中的特殊字符
        for symple in symple_set:
            item = item.replace(symple,'') 
        #如果在字典里，频次+1，否则写进字典
        word_list.append(item)
    return(Counter(word_list).most_common(count))
    # 排序        
    # return sorted(word_dict.items(),key = lambda x:x[1],reverse = True)
  

# 函数接受⼀一 个字符串串 text 作为参数, 统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列的数组
def stats_text_cn(text,count):
    if not isinstance(text,str):
        raise ValueError("text is not a string")
    seg_list = jieba.cut(text,cut_all=False) #精确模式
    chars = []
    # 排除长度小于2的词语
    for item in seg_list:
        if len(item) > 1:
            chars.append(item)          
    return Counter(chars).most_common(count)

# 如果输⼊入参数不不为字符串串类型则抛出 ValueError 错误，并包含完整的错误提示信息
def stats_text(text,count): 
    if not isinstance(text,str):
        raise ValueError("text is not a string")    
    print(stats_text_en(text,count),stats_text_cn(text,count))
