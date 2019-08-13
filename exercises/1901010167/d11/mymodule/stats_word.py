import  re 
import jieba
from collections import Counter
def  stats_text_en(text,count):
    if type(text) !=str:                                              #判断输入的text参数是否为字符串，不是则抛出valueerror异常
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        a=re.sub(r'[^A-Za-z]',' ',text)                               #只取英文单词
        newlist=a.split()                                             #单词划分                          
        return Counter(newlist).most_common(count)                    #返回英文单词频数统计结果

def stats_text_cn(content,count):
    if type(content)!=str:                                               #判断输入的content参数是否为字符串，不是则抛出valueerror异常
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        a=re.sub(r'[^A-Za-z]',' ',content)                               #获取content中的英文单词
        newlist=a.split()                                                #用空格进行切割，获得英文单词列表
        seg_list = jieba.lcut(content, cut_all=False)                    #用精确模式对content进行分词，得到分词列表
        words= [seg for seg in seg_list if len(seg) >=2 ]                #从分词列表获取长度大于2的单词
        words2= [word for word in words if (word not in newlist) ]       #从大于2的单词列表内获取非英语单词
        return  Counter(words2).most_common(count) 
                                       
def stats_text(text,count_cn,count_en):
    if type(text) != str:                                             #判断输入的text参数是否为字符串，不是则抛出valueerror异常
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        return stats_text_cn(text,count_cn),stats_text_en(text,count_en)

def stats_file(path,mode,count_cn,count_en):
    file=open(path,mode,encoding='utf-8')
    content=file.read()
    #print(content)
    file.close()
    return stats_text(content,count_cn,count_en)    

    
    
    