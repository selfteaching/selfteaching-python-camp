
from collections import Counter 
import re 
def stats_text_en(text):        #定义函数
        if type(text)!=str:
                raise ValueError('参数输入错误,请输入字符串')
     
        text=re.sub('[^A-Za-z]',' ',text).split()
        cnt=Counter(text).most_common(int(input('please type the amount of english words you want to display:')))
        return cnt                                          




#=================================================================任务2================================================================

def stats_text_cn(text):
        if type(text)!=str:
                raise ValueError('参数输入错误,请输入字符串')
        text=re.findall(u'[\u4e00-\u9fa5]',text)
        cnt=Counter(text).most_common(int(input('请输入需要显示的中文汉字数量:'))) 
        
        return cnt



def stats_text(text):
        if type(text) != str:
                raise ValueError('参数输入错误,请输入字符串')
        print(stats_text_en(text)+stats_text_cn(text))
     








