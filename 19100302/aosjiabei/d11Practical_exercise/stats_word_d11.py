import collections
import jieba
import re#导入正则表达式模块

#统计中文词频

def stats_text_cn(text):
    if not isinstance(text,str):#判断参数类型
        raise ValueError("text非字符串参数")#抛出异常类型
    #提取中文字符串
    text= re.sub("[^\u4e00-\u9fa5]", "", text)#中文汉字unicode范围
    text=jieba.cut(text)#jieba精准模式分词
    found=[]
    for x in text:
        if len(x)>=2:
            found.append(x)
    return collections.Counter(found).most_common(100)
    
    



            


