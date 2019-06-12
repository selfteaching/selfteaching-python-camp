import jieba
import re
import json
import sys
import collections
from collections import Counter
sys.path.append("c:")
# import stats_word

# with open("mymodule/tang300.json", "r", encoding="utf-8") as file:
#     try:
#         read_data = file.read()
#     except ValueError as e:
#         print(e)
def stats_text_en(en,count) :
    ''' 1. 英文词频统计：使用正则表达式过滤英文字符，使用Counter统计并排序。
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(en) == str : 
        text_en = re.sub("[^A-Za-z]", " ", en.strip())
        # text_en = ''.join(text_en)        
        enList = text_en.split( )
        return  collections.Counter(enList).most_common(count)
    else : 
        raise ValueError ('type of argumengt is not str')
# print(stats_text_en(read_data, 4))

def stats_text_cn(cn,count) :
    ''' 1. 使用jieba第三方库精确模式分词。
        2. 使用正则表达式过滤汉字字符。
        3. 使用for循环判断分词后词频列表元素长度大于等于2的生成新列表。
        4. 使用标准库collections.Counter()统计词频并限制统计数量。 
        5. 参数类型检查，不为字符串抛出异常。
    '''
    if type(cn) == str : 
            cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
            
            cnString = ''.join(cnList)
            
            segList = jieba.cut(cnString,cut_all=False)
            
            cnnewList = []
            for i in segList :
                    if len(i) >= 2 :
                            cnnewList.append(i)
                    else :
                            pass                
            return collections.Counter(cnnewList).most_common(count)
            
    else :
            raise ValueError ('type of argumengt is not str')
# print(stats_text_cn(read_data, 2))

def stats_text(text_en_cn,count_en_cn) :
    ''' 1. 合并英汉词频统计：调用stats_text_en()和stats_text_cn()并合并其结果。
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(text_en_cn) == str : 
            return stats_text_en(text_en_cn,count_en_cn)+stats_text_cn(text_en_cn,count_en_cn)
    else :
            raise ValueError ('type of argumengt is not str')

# print('输出词频最高的前20个中文词：\n ', stats_text_cn(read_data,20))