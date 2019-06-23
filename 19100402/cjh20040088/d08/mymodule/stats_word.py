def stats_text_en(text):
    if type(text) == str:
        text=text.replace(',','').replace('.','').replace('--','').replace('!','').replace('*','')
        text=text.split()
        b={}
        for i in text:
            b[i]=text.count(i)
            return b 
        result=sorted(stats_text_en(text).items(),key=lambda x:x[1],reverse=True)
        print(result)
    else:
        raise ValueError






def stats_text_cn(text): 
    if type(text)==str: 
        text=text.replace('，','').replace('、','').replace('。','')       
        c={}
        for i in text:
            u'\u4e00'<=i<=u'\u9fff'
            c[i]=text.count(i)
            return c
        result1=sorted(stats_text_cn(text).items(),key=lambda x:x[1],reverse=True)
        print(result1)        
    else:
        raise ValueError



def stats_text(text):
     stats_text_en(text)
     stats_text_cn(text)