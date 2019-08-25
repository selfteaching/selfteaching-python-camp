import  re 
import  collections 
def  stats_text_en(text):
    a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词
    newlist=a.split()                      #单词划分
    return(collections.Counter(newlist))  #输出英文单词频数统计结果


def stats_text_cn(text):
    words= [i for i in text if '\u4e00' <= i <= '\u9fa5']         #中文的Unicode编码范围为：[\u4e00-\u9fa5]，由此可获得字符串中的汉字列表   
    word_set=set(words)                                           #把汉字列表转换为集合去重，
    d={}
    for w in word_set:                                            #遍历汉字结合，用count方法可以直接判断出每个汉字在字符串中存在的个数
        c=words.count(w)
        d[w]=c                                                    #以汉字为键，个数c为值添加到字典d中
    return(sorted(d.items(),key=lambda d:d[1],reverse=True))    #对字典以键排序，获得排序后的列表，元素为键值对组成的元组
                            
def stats_text(text):
    return(print(stats_text_cn(text),stats_text_en(text)))
    

    
    
    