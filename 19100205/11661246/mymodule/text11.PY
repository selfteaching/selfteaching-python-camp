import collections
import re
def stats_text_en(en,count):  
    '''英文词频统计'''
    '''参数类型检查；如果输入参数不为字符串则抛出ValueError'''
    if type(en)== str: # 判断输入的是字符，执行以下语句

         text_en = re.sub("[A-Za-z]"," ", en.strip()) #只保留字母，并用空格作为分隔符
         enlist=text_en.split() #以空格和折行为分隔，将每个被分割的内容作为一个列表的元素，并将所有列表元素和在一起，组成一个列表
         return collections.Counter(enlist).most_common(count)
         #利用coletions中的counter为每个出现的英文单词计数，返回前count个词频最高的词及出现的次数
    else:
         raise ValueError("输入的不是字符串")   

def stats_text_cn(cn,count):
    '''中文汉字字频统计'''
    '''参数类型检查；如果输入参数不为字符串则抛出ValueError'''    
    if type(cn)== str: # 判断输入的是字符，执行以下语句

         text_cn = re.findall(u'[\4e00-\u9fff]+',cn.strip()) #只保留字母，并用空格作为分隔符
         cnlist=text_cn.split() #以空格和折行为分隔，将每个被分割的内容作为一个列表的元素，并将所有列表元素和在一起，组成一个列表
         seg_list = jieba.cut(' '.join(cnlist))
         cn1 = []
         for i in seg_list:
              if len(i) >= 2:
                   cn1.append(1)
         return collections.Counter(cnlist).most_common(count)
                        #利用coletions中的counter为每个出现的中文汉字计数，返回前count个词频最高的词及出现的次数
    else:
         raise ValueError("输入的不是字符串")   

def stats_text(text_e_c,count_e_c):
    '''合并英汉词频统计'''
    '''参数类型检查，如果输入参数不为字符串则抛出ValueError'''
    if type(text_e_c) == str:
         return(stats_text_en(text_e_c,count_e_c)+stats_text_cn(text_e_c,count_e_c))
    else:
         raise ValueError("输入的不是字符串")
        
           
