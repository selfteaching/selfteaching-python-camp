import  re 
import  collections  
count = int()

#\u4e00-\u9fa5 	汉字的unicode范围
#\u0030-\u0039 	数字的unicode范围
#\u0041-\u005a 	大写字母unicode范围
#\u0061-\u007a 	小写字母unicode范围

from collections import Counter

def stats_text_en(text,count):              #定义函数
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    text_d = []
    text_a=text.replace(',',' ').replace('--',' ').replace('*',' ').replace('!',' ').replace('.',' ').replace('—',' ').replace('。',' ').replace('《','').replace('》','').replace('，',' ')     #删除标点符号
    text_b=text_a.lower()                                                                          
    text_c=text_b.split()
    for i in text_c:
        if u'\u0041' <= i <= u'\u005a':
            text_d.append(i) 
        elif u'\u0061' <= i <= u'\u007a':
            text_d.append(i)
    return Counter(text_d).most_common(count)  






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
    return collections.Counter(text1).most_common(count)
    





def stats_word(text,count): #定义函数，实现统计汉字和英文单词出现次数
    if type(text)!=str:
        raise ValueError("文本为非字符串")
    
    return stats_text_en(text,count) + stats_text_cn(text,count)








