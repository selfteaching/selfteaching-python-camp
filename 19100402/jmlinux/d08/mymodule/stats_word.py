import collections 
import re

def stats_text_en(str_en):   #函数实现统计每个英文单词出现的次数，返回一个按词频降序排列的数组
    if isinstance(str_en, str):     #参数类型检查
        #print(isinstance(str_en, str))
        str_en = re.sub("[^A-Za-z]", " ", str_en.strip())   #过滤英文字符外的字符
        list1 = str_en.split()  #分割单词
        return collections.Counter(list1)    #统计并返回结果
    else : 
        raise ValueError ('type of argumengt is not str')  #不为字符串抛出异常
def stats_text_cn(str_cn):   # 函数实现统计中文汉字出现的次数，返回一个按词频降序排列的数组统计
    if isinstance(str_cn, str):  #参数类型检查
        str1 = re.findall(u'[\u4e00-\u9fff]+', str_cn)   #过滤汉字字符
        str2 = ''.join(str1)  
        return collections.Counter(str2)   #统计并返回结果
    else : 
        raise ValueError ('type of argumengt is not str')  #不为字符串抛出异常

def stats_text(text):
    if isinstance(text, str):   #参数类型检查`
        return(stats_text_en(text)+stats_text_cn(text))  #返回
    else : 
        raise ValueError ('type of argumengt is not str')  #不为字符串抛出异常
#if __name__ == '__main__':
#    stats_text(text)
    