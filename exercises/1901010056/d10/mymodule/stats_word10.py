import  re 
import  collections  
count = int()
#英文词频统计函数
def  stats_text_en(text,count):
    if type(text) != str :
        raise ValueError ('type of argumengt is not str')

import jieba #导入第三方库
#中文词频统计函数
def  stats_text_cn(text,count):
    if type(text) != str : 
        raise ValueError ('type of argumengt is not str')


    text=re.sub('[^\u4e00-\u9fa5]','',text) #[^\u4e00-\u9fa5]表示所有非中文
    text=jieba.lcut(text)  #精确切分中文，返回一个list
    text1=[]
    for i in text: #筛选长度大于等于2的词
        if len(i)>=2:
            text1.append(i)
    print(collections.Counter(text1).most_common(count))

def stats_word(text,count): #定义函数，实现统计汉字和英文单词出现次数


 
    if type(text)!=str:


 
        raise ValueError("文本为非字符串")


 
    stats_text_en(text,count)


 
    stats_text_cn(text,count)


 










 