from collections import Counter 

def stats_text_en(a,count):  
    a=a.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ')
    a=a.split() 
    if type(a) != str:                  
        raise ValueError('ValuError:it is not string')
    number = Counter()
    for s in a:  
        if s.isascii():
            number[s]+=1

    return Counter(number).most_common(count)  

def stats_text_cn(x,count): 
    j={}
    if type(x)!=str:                  
        raise ValueError('ValuError:it is not string')   
    x=x.replace('，','').replace('。','').replace('!','').replace('*','').replace('-','').replace('?','') 
    j=''.join(x)

    
    number = Counter()

    for e in j :                   
        if '\u4e00' <= e <= '\u9fff' :
            number[e]+=1
    return Counter(number).most_common(count)

def stats_text(a,count):
    if type(a) !=str:                   
        raise ValueError('ValuError:it is not string')
    print(stats_text_cn(a,count))  
    print(stats_text_en(a,count)) 