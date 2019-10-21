import collections
import re
import jieba


# 将中文进行词频统计。
def stats_text_cn(text,count):
    if type(text) == str:
        # 筛选出文本中所有的中文字符  
        list1 = re.findall(r'[\u4e00-\u9fa5]', text)    
        # 将列表转化成字符串
        string1 = "".join(list1)    
        # 使用结巴对字符串进行分词
        list2 = jieba.lcut(string1)    
        # 将分词的结果进行处理，去除长度为1的中文词汇
        list3 = list2[:]    
        for i in list2:
            if len(i) == 1:
                list3.remove(i)
        list2 = list3
        # 将处理过的分词结果进行排序
        word_frequencycount_cn_list = collections.Counter(list2).most_common(count)  
        # 将结果转化为字符串
        word_frequencycount_cn_str = str(word_frequencycount_cn_list)  
        return word_frequencycount_cn_str
    else:
        raise ValueError("The input is a non-string, please enter a string.")