import collections
import jieba
import re   #正则表达(regular expression)
#定义函数用于统计英文单词词频，并按词频降序输出，extract English words from string in python
def stats_text_en(text,count):
    if type(text) == str:
        result = re.sub("[^A-Za-z]", " ", text.strip()) #只取英文，不需要考虑标点符号，无需replace
        newList = result.split() #划分合并单词
        return collections.Counter(newList).most_common(count)

print()
#定义函数用于统计中文汉字字频，并按字频降序输出
def stats_text_cn(text,count): 
    if type(text) == str:
        result_1 = re.findall(u'[\u4e00-\u9fff]+', text) #只取中文，不需要考虑标点符号，无需replace
        newString = ''.join(result_1) #组合成字符串
        seg_list =[ x for x in jieba.cut_for_search(newString) if len(x) >= 2]
        return collections.Counter(seg_list).most_common(count)
        
        
   
print()
#输出中英文合并词频统计结果
def stats_text(text,count):
    return(stats_text_en(text,count),stats_text_cn(text,count))

