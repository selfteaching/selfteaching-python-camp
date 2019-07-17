import  re 
from collections import Counter
import  jieba


#英文词频统计函数
def  stats_text_en(text,count):
    if type(text) == str :
        a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词
        newlist=a.split()                      #单词划分
        return(Counter(newlist).most_common(count))  #输出英文单词频数统计结果
    else:
        print('stats_text_en函数：出现ValueError,传入的参数非字符串' ) 


#中文词频统计函数
def  stats_text_cn(text,count):
    if type(text) == str :
        p =  re.compile(r'[\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
        res = re.findall(p, text)   #取中文
        cn=''.join(res)           #中文拼接
        newcn=jieba.cut(cn)  #结巴分词
        c = Counter()
        for x in newcn:
            if len(x)>1 :
               c[x] += 1
        return(c.most_common(count))   #输出中文词频统计结果
    else:
        print('stats_text_cn函数：出现ValueError,传入的参数非字符串' ) 

#分别调用stats_text_en、stats_text_cn，并合并输出词频统计结果
def  stats_text(text,count):
    if type(text) == str :
        print(stats_text_en(text,count)+stats_text_cn(text,count))
    else:
        print('stats_text函数：出现ValueError,传入的参数非字符串' ) 

