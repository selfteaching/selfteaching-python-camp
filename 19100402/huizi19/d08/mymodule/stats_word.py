import  re 
import  collections  



#英文词频统计函数
def  stats_text_en(text):
    if type(text) == str :
        a=re.sub(r'[^A-Za-z]',' ',text)    #只取英文单词
        newlist=a.split()                      #单词划分
        return(collections.Counter(newlist))  #输出英文单词频数统计结果
    else:
        print('stats_text_en函数：出现ValueError,传入的参数非字符串' ) 

#中文词频统计函数
def  stats_text_cn(text):
    if type(text) == str :
        p =  re.compile(r'[\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
        res = re.findall(p, text)   #取中文
        newcn=''.join(res)
        return(collections.Counter(newcn))  #输出中文词频统计结果
    else:
        print('stats_text_cn函数：出现ValueError,传入的参数非字符串' ) 

#分别调用stats_text_en、stats_text_cn，并合并输出词频统计结果
def  stats_text(text):
    if type(text) == str :
        print(stats_text_en(text)+stats_text_cn(text))
    else:
        print('stats_text函数：出现ValueError,传入的参数非字符串' ) 


