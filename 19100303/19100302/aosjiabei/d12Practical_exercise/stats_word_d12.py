import collections
import jieba
import re#导入正则表达式模块

#统计中文词频

def stats_text_cn(text):
    #提取中文字符串
    text= re.sub("[^\u4e00-\u9fa5]", "", text)#中文汉字unicode范围
    text=jieba.cut(text)#jieba精准模式分词
    found=[]
    for x in text:
        if len(x)>=2:
            found.append(x)
    return collections.Counter(found).most_common(10)



            


