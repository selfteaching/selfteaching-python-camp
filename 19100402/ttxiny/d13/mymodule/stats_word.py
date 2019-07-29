import re  
import collections  
import jieba
def stats_text(txt,count):
       stats_text_cn(txt,count)
       stats_text_en(txt,count)

def stats_text_en(txt,count):
       if type(txt)==str:
              txt=re.sub('[^a-zA-Z]',' ',txt.strip())
              txt=txt.split()
              print(collections.Counter(txt).most_common(count))
       else:
              raise ValueError
      
def stats_text_cn(txt,count):
    import re
    if type(txt) == str:
           txt=re.sub('[^\u4e00-\u9fa5]','',txt)
           txt=txt.strip()
           txt=jieba.cut(txt,cut_all=False)
           txtnew=collections.Counter()
           for i in txt:
                  if len(i)>=2:
                         txtnew[i]+=1        
           print(txtnew.most_common(count))
    else:
           raise ValueError
