import re
from collections import Counter
import jieba
# 统计英文

def stats_text_en(content,count):   #定义一个函数stats_en
    if not isinstance(content,str):  #一个if语句用来判断text是否是字符串，否则的话生成一个异常
        raise ValueError('参数必须是str类型')
    word_list = re.findall(r'\b[a-z]+\'?[a-z]+',content.lower())  #代码是参考了别人的，请看一下如何把一片文档中的所有英文单词单独提炼出来，请google
    return Counter(word_list).most_common(count)

# 统计中文
def stats_text_cn(content,count):
    if not isinstance(content,str):
        raise ValueError('参数必须是str类型')
    cn = re.sub(r'[\Wa-zA-Z0-9]','',content) 
    cn_1 = jieba.cut(cn, cut_all=False)  #用jieba第三方库对cn进行分词而不是分字
    list_cn = []  #建立一个空列表，为下一个循环使用
    for i in cn_1:
        if len(i)>= 2:
            list_cn.append(i)

    return Counter(list_cn).most_common(count)

def stats_text(content,count):
    list_en = stats_text_en(content,count)
    list_cn = stats_text_cn(content,count)

    return list_en + list_cn


