import  re 
import  collections  
count = int()
#英文词频统计函数
def  stats_text_en(text,count):
    if type(text) == str :
            a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词
            newlist=a.split()                      #单词划分
            return(collections.Counter(newlist).most_common(count))  #输出英文单词频数统计结果
    else :
            raise ValueError ('type of argumengt is not str')


#中文词频统计函数
def  stats_text_cn(text,count):
    if type(text) == str : 
            p =  re.compile(r'[\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
            res = re.findall(p, text)   #取中文
            newcn=''.join(res)
            return(collections.Counter(newcn).most_common(count))  #输出中文词频统计结果
    else:
            raise ValueError ('type of argumengt is not str')


#分别调用stats_text_en、stats_text_cn，并合并输出词频统计结果
def  stats_text(text,count):
    if type(text)==str:
            return(stats_text_en(text,count,count)+stats_text_cn(text,count,count))  
    else:
            raise ValueError ('type of argumengt is not str')







 