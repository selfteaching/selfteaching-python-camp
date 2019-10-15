import  re 
from collections import Counter
def  stats_text_en(text,count):
    if type(text) !=str:                                              #判断输入的text参数是否为字符串，不是则抛出valueerror异常
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        a=re.sub(r'[^A-Za-z]',' ',text)                               #只取英文单词
        newlist=a.split()                                             #单词划分                          
        return Counter(newlist).most_common(count)                    #返回英文单词频数统计结果

def stats_text_cn(text,count):
    if type(text)!=str:                                               #判断输入的text参数是否为字符串，不是则抛出valueerror异常
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        words= [i for i in text if '\u4e00' <= i <= '\u9fa5']         #中文的Unicode编码范围为：[\u4e00-\u9fa5]，由此可获得字符串中的汉字列表
        return Counter(words).most_common(count)
                                
def stats_text(text,count_cn,count_en):
    if type(text) != str:                                             #判断输入的text参数是否为字符串，不是则抛出valueerror异常
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        return stats_text_cn(text,count_cn),stats_text_en(text,count_en)

def stats_file(path,mode,count_cn,count_en):
    file=open(path,mode,encoding='utf-8')
    content=file.read()
    print(content)
    print(stats_text(content,count_cn,count_en))
    file.close()
        

    
    
    