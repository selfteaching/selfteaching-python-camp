
from collections import Counter 
import jieba
import re 
def stats_text_en(text,count):        #定义函数
        if type(text)!=str:
                raise ValueError('参数输入错误,请输入字符串')
     
        text=re.sub('[^A-Za-z]',' ',text).split()
        cnt=Counter(text).most_common(int(count))
        return cnt                                          




#=================================================================任务2================================================================

def stats_text_cn(text,count):
        if type(text)!=str:
                raise ValueError('参数输入错误,请输入字符串')
        text=re.findall(u'[\u4e00-\u9fa5]',text)
        text="".join(text)
        seg1=jieba.cut(text)
        seg2=[]       
        for i in seg1:
                if len(i)>=2:
                        seg2.append(i)

        cnt=Counter(seg2).most_common(int(count))
        
        return cnt



def stats_text(text,count):
        if type(text) != str:
                raise ValueError('参数输入错误,请输入字符串')
        return(stats_text_en(text,count)+stats_text_cn(text,count))
     



