import  re 
import jieba
from collections import Counter

def  stats_text_en(text,count):
    if type(text) !=str:
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        a=re.sub(r'[^A-Za-z]',' ',text)
        newlist=a.split()          
        return Counter(newlist).most_common(count) 

def stats_text_cn(filename,count):
    file=open(filename,'r',encoding='utf-8') 
    content=file.read()                     
    if type(content)!=str:                                     
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        a=re.sub(r'[^A-Za-z]',' ',content)                        
        newlist=a.split()                                     
        seg_list = jieba.lcut(content, cut_all=False)                 
        words= [seg for seg in seg_list if len(seg) >=2 ]          
        words2= [word for word in words if (word not in newlist) ]
        print ( Counter(words2).most_common(count)) 
        file.close()
                     
def stats_text(text,count_cn,count_en):
    if type(text) != str:                                         
        raise ValueError("输入的为非字符串，请输入字符串")
    else:
        return stats_text_cn(text,count_cn),stats_text_en(text,count_en)

def stats_file(path,mode,count_cn,count_en):
    file=open(path,mode,encoding='utf-8')
    content=file.read()
    print(content)
    print(stats_text(content,count_cn,count_en))
    file.close()