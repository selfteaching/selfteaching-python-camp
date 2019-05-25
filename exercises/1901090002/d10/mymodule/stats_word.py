from collections import Counter 
import jieba

def stats_text_en(text,count):  
    text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    text=text.split() 
    if type(text) != str:                  
        raise ValueError('ValuError:it is not string')
    number = Counter()
    for s in text:  
        if s.isascii():
            number[s]+=1

    return Counter(number).most_common(count)  

def stats_text_cn(text,count): 
    j={}
    if type(text)!=str:                  
        raise ValueError('ValuError:it is not string')   
    text=text.replace('，','').replace('。','').replace('!','').replace('*','').replace('-','').replace('?','') 
    j=''.join(text)
    text = [x for x in jieba.cut(j,cut_all=False ) if len(x) >=2] #jieba精准模式
    # print("Default Mode:"+"/".join(text))
    
    number = Counter()

    for e in j :                   
        if '\u4e00' <= e <= '\u9fff' :
            number[e]+=1
    return Counter(number).most_common(count)

#def stats_text(text,count):
 #   if type(text) !=str:                   
#      raise ValueError('ValuError:it is not string')
 #   print(stats_text_cn(text,count))  
#  print(stats_text_en(text,count)) 