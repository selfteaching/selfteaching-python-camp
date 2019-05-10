
import re
import collections
import jieba

count = int()

def stast_text_en(text,count):
    ''' 统计英文单词词频出现的次数 '''
    if type(text) == str:
        text = re.sub("[^A-Za-z]", " ", text) #用正则表达式中的sub方法替换所有非英文字母为空格
        text = text.split()
        return(collections.Counter(text).most_common(count))
    else:
        raise ValueError('此文本为非字符串')
    
def stast_text_cn(text,count):
    ''' 统计中文词频出现的次数 '''
    if type(text) == str:
        text = re.findall(u'[\u4e00-\u9fff]+',text)
        seg_list = jieba.cut(' '.join(text))
        cn_list = []
        for i in seg_list:
            if len(i) > 1:
                cn_list.append(i)  
        return(collections.Counter(cn_list).most_common(count))
    else:
        raise ValueError('此文本为非字符串')

def stast_text(text,count):
    ''' 统计中文和英文词频出现的次数 '''
    if type(text) == str:
        print(stast_text_en(text,count)+stast_text_cn(text,count))
    else:
        raise ValueError('此文本为非字符串')
